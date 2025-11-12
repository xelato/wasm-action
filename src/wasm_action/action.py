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
from .util import format_package, parse_package
from .model import Action, RegistryType
from .warg_pull import warg_pull


def error(text):
    return ValueError(text)

@click.group()
def cli():
    pass


@cli.command(help="Push to a WebAssembly registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--namespace', required=True, help="package namespace")
@click.option('--name', required=True, help="package name")
@click.option('--version', required=True, help="package version")
@click.option('--path', required=True, help="filename")
def push(registry, namespace, name, version, path):

    if not path:
        raise error('path is required')

    # expand path pattern into filename, ensure only a single file
    files = glob.glob(path)
    if not files:
        raise error('file not found: {}'.format(path))
    if len(files) > 1:
        raise error('more than one files found: {}'.format(path))

    filename = files[0]

    # extract version from filename if not provided
    if not version:
        version = extract_version(filename)

    # validate version as semver
    semver.Version.parse(version)


    # validate key
    key = os.environ.get('WARG_PRIVATE_KEY')
    if not key:
        raise error('no key provided')

    try:
        PrivateKey.load(key)
    except:
        raise error("Error loading private key")
    else:
        print("valid private key")

    # todo: implement push


@cli.command(help="Pull from a WebAssembly registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=False, help="filename")
def pull(registry, package, path=None):

    if not package:
        raise error("package is required")

    namespace, name, version = parse_package(package)

    settings = validate_registry(registry)

    if settings.get('registry-type') != RegistryType.WARG:
        raise error("Registry type not supported: {}".format(settings.get('registry-type')))

    download = warg_pull(registry, settings['warg-url'], namespace, name, version)

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
