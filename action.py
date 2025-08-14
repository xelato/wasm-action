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
import pexpect


def error(text):
    return ValueError(text)

@click.group()
def cli():
    pass


@cli.command(help="Validate package")
@click.option('--path', required=True, help="package path, glob pattern supported")
@click.option('--namespace', required=True, help="package namespace")
@click.option('--name', required=True, help="package name")
@click.option('--version', required=False, help="package version (optional)")
def package(path, namespace, name, version):

    if not path:
        raise error('path is required')

    if not namespace:
        raise error('namespace is required')

    if not name:
        raise error('name is required')

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

    # job outputs
    with open(filename, 'rb') as f:
        digest = "sha256:{}".format(hashlib.file_digest(f, "sha256").hexdigest())

    add_github_output('filename', filename)
    add_github_output('digest', digest)
    add_github_output('namespace', namespace)
    add_github_output('name', name)
    add_github_output('version', version)


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
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write('{key}={value}\n'.format(key=key, value=value))


def extract_version(filename):
    """Extract version from a filename.
    Return the substring between the last '@' and last '.'"""
    s = os.path.basename(filename)
    return s[s.rfind('@')+1:s.rfind('.')]


@cli.command(
    help="Wrapper for warg command",
    context_settings={
        "ignore_unknown_options": True,
        "allow_extra_args": True,
    })
def warg():
    argv = sys.argv[2:]

    command = ['warg']
    command.extend(argv)

    print("$ {}".format(' '.join(command)))

    # warg key set
    if command == ['warg', 'key', 'set']:
        key = os.environ.get('WARG_PRIVATE_KEY')
        if not key:
            raise error('no key provided')
        if key.count(':') != 1:
            raise error('expected key format ecdsa-p256:<key>')
        alg, value = key.split(':')
        if alg != 'ecdsa-p256':
            raise error('alg ecdsa-p256 expected')
        # private key has length 32
        # public key has length 33
        if len(base64.b64decode(value)) != 32:
            raise error('unexpected private key length')
        print("valid private key")

        p = pexpect.spawn(' '.join(command))
        p.expect('input signing key')
        p.expect(':')
        p.expect(':')
        import time
        time.sleep(1)
        p.sendline(key)
        p.expect(pexpect.EOF)
        p.wait()
        return p.exitstatus

    # warg login
    elif argv == ['warg', 'login']:
        pass

    # default
    else:
        p = pexpect.spawn(' '.join(command))
        p.logfile = sys.stdout.buffer
        p.expect(pexpect.EOF)
        p.wait()
        return p.exitstatus


def main():
    cli()


if __name__ == "__main__":
    main()
