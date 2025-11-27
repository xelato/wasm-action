import sys
import enum
import glob
import os
import hashlib
import base64

import click
import semver
import validators
import requests

from . import warg_proto
from .warg_crypto import PrivateKey
from .warg_client import WargClient
from .util import add_github_output, detect_registry_settings, RegistryType
from .util import format_package, parse_package, extract_version
from .model import Action, RegistryType
from .warg_pull import warg_pull, warg_push


def error(text):
    return ValueError(text)

@click.group()
def cli():
    pass


@cli.command(help="Push to registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=True, help="filename")
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token")
@click.option('--warg-private-key', required=False, envvar='WARG_PRIVATE_KEY', help="warg private key")
def push(registry, package, path, warg_token, warg_private_key):

    # path
    if not path:
        raise error('path is required')

    # glob pattern support: (ex.: package-*.wasm)
    # expand path pattern into filename, ensure only a single file
    files = glob.glob(path)
    if not files:
        raise error('file not found: {}'.format(path))
    if len(files) > 1:
        raise error('more than one files found: {}'.format(path))
    filename = files[0]

    # package
    if not package:
        raise error("package is required")

    namespace, name, version = parse_package(package)

    # extract version from filename if not provided
    if not version:
        version = extract_version(filename)

    # validate version as semver
    semver.Version.parse(version)

    settings = validate_registry(registry)
    if settings.get('registry-type') != RegistryType.WARG:
        raise error("Registry type not supported: {}".format(settings.get('registry-type')))

    # validate private key
    if not warg_private_key:
        raise error('no private key provided')

    try:
        private_key = PrivateKey.load(warg_private_key)
    except:
        raise error("Error loading private key")

    # push
    warg_push(registry, settings['warg-url'], namespace, name, version, filename, warg_token, warg_private_key)


@cli.command(help="Pull from registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=False, help="filename")
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token")
def pull(registry, package, path=None, warg_token=None):

    if not package:
        raise error("package is required")

    namespace, name, version = parse_package(package)

    settings = validate_registry(registry)

    if settings.get('registry-type') != RegistryType.WARG:
        raise error("Registry type not supported: {}".format(settings.get('registry-type')))

    download = warg_pull(registry, settings['warg-url'], namespace, name, version, warg_token=warg_token)

    filename = path or "{}:{}@{}.wasm".format(namespace, name, download.version)
    with open(filename, 'wb') as f:
        f.write(download.content)

    add_github_output('package', format_package(namespace=namespace, name=name, version=download.version))
    add_github_output('package-namespace', download.namespace)
    add_github_output('package-name', download.name)
    add_github_output('package-version', download.version)
    add_github_output('digest', download.digest)
    add_github_output('filename', filename)


def validate_registry(registry):
    if not registry:
        raise error('registry is required')

    if not validators.domain(registry, consider_tld=True):
        raise error('registry is not a valid domain name: "{}"'.format(registry))

    add_github_output('registry', registry)
    settings = detect_registry_settings(registry)
    for key, value in settings.items():
        add_github_output(key, str(value))
    return settings


def main():
    cli()


if __name__ == "__main__":
    main()
