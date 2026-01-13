import sys
import enum
import glob
import os
import hashlib
import base64
import json

import click
import semver
import validators
import requests

from .registry import RegistryType, detect_registry_settings
from .util import add_github_output, format_package, parse_package, extract_version
from .warg.crypto import PrivateKey
from .warg.client import WargClient
from .warg.actions import warg_pull, warg_push


def error(text):
    return ValueError(text)


def push_file(registry, package, path, warg_token, warg_private_key, cli=False):
    """Push file to registry"""

    # path
    if not path:
        raise error('path is required')

    # glob pattern support: (ex.: package-*.wasm)
    # expand path pattern into filename, ensure only a single file
    files = glob.glob(path)
    if not files:
        raise error('file not found: {}'.format(path))
    if len(files) > 1:
        raise error('more than one file found: {}'.format(path))
    filename = files[0]

    # extract version from filename if not provided
    namespace, name, version = parse_package(package)
    if not version:
        version = extract_version(filename)
        package = format_package(namespace, name, version)

    with open(filename, 'rb') as f:
        content_bytes = f.read()

    return push(registry, package, content_bytes, warg_token, warg_private_key, cli=cli)


def push(registry, package, content_bytes, warg_token, warg_private_key, cli=False):
    """Push to registry"""

    # package
    if not package:
        raise error("package is required")

    namespace, name, version = parse_package(package)
    if not version:
        raise error("version is required")

    # validate version as semver
    semver.Version.parse(version)

    settings = validate_registry(registry, cli=cli)
    if settings.get('registry-type') != RegistryType.WARG:
        raise error("Registry type not supported: {}".format(settings.get('registry-type')))

    # validate private key
    if not warg_private_key:
        raise error('no private key provided')

    try:
        private_key = PrivateKey.load(warg_private_key)
    except:
        raise error("Error loading private key")
    else:
        if cli:
            add_github_output('key-id', private_key.public_key().fingerprint())
            add_github_output('public-key', private_key.public_key().canonical())

    if warg_token and '/' in warg_token:
        v = warg_token.split('/', 1)[1]
        if cli:
            add_github_output('token-id', "sha256:{}".format(hashlib.sha256(v.encode('utf8')).hexdigest()))

    # push
    try:

        record = warg_push(
            registry, settings['warg-url'],
            namespace, name, version, content_bytes,
            warg_token, warg_private_key)

    except Exception as e:
        message = str(e)
        if hasattr(e, 'body'):
            message = str(e.body)
            try:
                message = json.loads(e.body)['message']
            except:
                pass
        if cli:
            add_github_output('error', message)
        raise

    if cli:
        add_github_output('state', record['state'])
        add_github_output('package', format_package(namespace=record['namespace'], name=record['name'], version=record['version']))
        add_github_output('package-namespace', record['namespace'])
        add_github_output('package-name', record['name'])
        add_github_output('package-version', record['version'])
        add_github_output('package-record-id', record['record_id'])

    return record


def pull(registry, package, warg_token=None, cli=False):
    """Pull from registry"""

    if not package:
        raise error("package is required")

    namespace, name, version = parse_package(package)

    settings = validate_registry(registry, cli=cli)

    if settings.get('registry-type') != RegistryType.WARG:
        raise error("Registry type not supported: {}".format(settings.get('registry-type')))

    download = warg_pull(registry, settings['warg-url'], namespace, name, version, warg_token=warg_token)

    return download


def pull_file(registry, package, path=None, warg_token=None, cli=False):
    """Pull from registry, write to file"""

    download = pull(registry, package, warg_token, cli=cli)

    filename = path or "{}:{}@{}.wasm".format(download.namespace, download.name, download.version)
    with open(filename, 'wb') as f:
        f.write(download.content)

    if cli:
        add_github_output('package', format_package(
            namespace=download.namespace, name=download.name, version=download.version))
        add_github_output('package-namespace', download.namespace)
        add_github_output('package-name', download.name)
        add_github_output('package-version', download.version)
        add_github_output('digest', download.digest)
        add_github_output('filename', filename)


def validate_registry(registry, cli=False):
    if not registry:
        raise error('registry is required')

    if not validators.domain(registry, consider_tld=True):
        raise error('registry is not a valid domain name: "{}"'.format(registry))

    if cli:
        add_github_output('registry', registry)
    settings = detect_registry_settings(registry)
    if cli:
        for key, value in settings.items():
            add_github_output(key, str(value))
    return settings
