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

import warg_proto
from warg_crypto import PrivateKey
from warg_client import WargClient



class Action(enum.Enum):
    PUSH = 'push'
    PULL = 'pull'

    def __str__(self):
        return self.value


def error(text):
    return ValueError(text)

@click.group()
def cli():
    pass


@cli.command(help="Validate action")
@click.option('--action', required=True, help="requested action", type=Action)
def action(action):
    add_github_output('action', action.value)


@cli.command(help="Validate package")
@click.option('--action', required=True, help="requested action to perform", type=Action)
@click.option('--path', required=True, help="package path, glob pattern supported")
@click.option('--namespace', required=True, help="package namespace")
@click.option('--name', required=True, help="package name")
@click.option('--version', required=False, help="package version (optional)")
def package(action, path, namespace, name, version=''):

    if not namespace:
        raise error('namespace is required')

    if not name:
        raise error('name is required')

    if version:
        # validate version as semver
        semver.Version.parse(version)

    if action == Action.PULL:
        # todo: file extension
        filename = path if path else (
            "{}-{}@{}.wasm".format(namespace, name, version) if version
            else "{}-{}.wasm".format(namespace, name)
        )

    elif action == Action.PUSH:
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

    else:
        pass

    add_github_output('namespace', namespace)
    add_github_output('name', name)
    add_github_output('version', version)
    add_github_output('filename', filename)


class RegistryType(enum.Enum):
    OCI = 'oci'
    WARG = 'warg'

    def __str__(self):
        return self.value


@cli.command(help="Validate registry")
@click.option('--registry', required=True, help="registry domain name")
def registry(registry):
    if not registry:
        raise error('registry is required')

    if not validators.domain(registry, consider_tld=True):
        raise error('registry is not a valid domain name: "{}"'.format(registry))

    # outputs
    add_github_output('registry', registry)
    for key, value in detect_registry_settings(registry).items():
        add_github_output(key, str(value))


def detect_registry_settings(registry):
    """Discovery based on .well-known domain config"""
    url = "https://{domain}/.well-known/wasm-pkg/registry.json".format(domain=registry)
    r = requests.get(url, timeout=10)
    if not r.ok:
        return {}

    data = r.json()

    result = {}
    if 'preferredProtocol' in data:
        if data['preferredProtocol'] == 'warg':
            result['registry-type'] = RegistryType.WARG
            if 'warg' in data:
                if 'url' in data['warg']:
                    result['warg-url'] = data['warg']['url']

        elif data['preferredProtocol'] == 'oci':
            result['registry-type'] = RegistryType.OCI
            if 'oci' in data:
                if 'registry' in data['oci']:
                    result['oci-registry'] = data['oci']['registry']
                if 'namespacePrefix' in data['oci']:
                    result['oci-namespace-prefix'] = data['oci']['namespacePrefix']

    elif 'wargUrl' in data:
        result['registry-type'] = RegistryType.WARG
        result['warg-url'] = data['wargUrl']

    elif 'ociRegistry' in data:
        result['registry-type'] = RegistryType.OCI
        result['oci-registry'] = data['ociRegistry']
        if 'ociNamespacePrefix' in data:
            result['oci-namespace-prefix'] = data['ociNamespacePrefix']

    return result


def add_github_output(key, value):
    """Add a github job output to the file pointed by the GITHUB_OUTPUT variable"""
    line = '{key}={value}\n'.format(key=key, value=value)
    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(line)
    else:
        sys.stdout.write(line)


def extract_version(filename):
    """Extract version from a filename.
    Return the substring between the last '@' and last '.'"""
    s = os.path.basename(filename)
    return s[s.rfind('@')+1:s.rfind('.')]


@cli.command(help="Push to a warg registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--warg-url', required=True, help="registry warg url")
@click.option('--filename', required=True, help="filename")
@click.option('--namespace', required=True, help="package namespace")
@click.option('--name', required=True, help="package name")
@click.option('--version', required=True, help="package version")
def warg_push(registry, warg_url, filename, namespace, name, version):
    print(registry)
    print(warg_url)
    print(filename)
    print(namespace)
    print(name)
    print(version)

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


@cli.command(help="Pull from a warg registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--warg-url', required=True, help="registry warg url")
@click.option('--filename', required=False, help="filename")
@click.option('--namespace', required=True, help="package namespace")
@click.option('--name', required=True, help="package name")
@click.option('--version', required=False, help="package version")
def warg_pull(registry, warg_url, filename, namespace, name, version):
    print(registry, warg_url)
    package = "{}/{}@{}".format(namespace, name, version)
    print(package)

    client = WargClient(
        registry=registry,
        warg_url=warg_url,
        access_token=os.environ.get('WARG_TOKEN'))

    res = client.get_checkpoint(namespace=namespace)
    print("\n", res)

    log_length = res.contents.log_length
    res = client.fetch_logs(namespace=namespace, name=name, log_length=log_length)
    print("\n", res)

    if not res.packages:
        raise error('failed to fetch logs')

    log_id, packages = res.packages.popitem()
    print(log_id)
    if not packages:
        raise error('failed to fetch logs')

    found_version, digest = find_version(packages, requested_version=version)

    if not digest or not found_version:
        raise error(
            'no package version found' if not version
            else 'requested version {} not found'.format(version))

    # get content sources
    res = client.get_content_sources(
        namespace=namespace,
        digest=digest
    )
    print("\n", res)

    if not res.content_sources:
        raise error('failed to fetch sources')
    digest, sources = res.content_sources.popitem()
    if not sources:
        raise error('failed to fetch sources')
    source = sources[0]
    url = source['url']

    # Fetch content from url with digest expected
    res = requests.get(url)
    content_digest = 'sha256:{}'.format(hashlib.sha256(res.content).hexdigest())
    if digest != content_digest:
        raise error('unexpected content digest')

    filename = "{}-{}@{}.wasm".format(namespace, name, version)
    with open(filename, 'wb') as f:
        f.write(res.content)


def find_version(packages, requested_version=None):
    version, digest = None, None
    for package in packages:
        record = warg_proto.PackageRecord()
        record.ParseFromString(base64.b64decode(package['contentBytes']))
        for entry in record.entries:

            obj = getattr(entry, entry.WhichOneof('contents'))

            if isinstance(obj, warg_proto.PackageRelease):

                if requested_version:
                    if obj.version == requested_version:
                        version = obj.version
                        digest = obj.content_hash
                else:
                    # latest version, assuming already ordered
                    version = obj.version
                    digest = obj.content_hash

    return version, digest


def main():
    cli()


if __name__ == "__main__":
    main()
