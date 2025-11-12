
import os
import re
import sys
import requests
import semver

from .model import RegistryType


def add_github_output(key, value):
    """Add a github job output to the file pointed by the GITHUB_OUTPUT variable"""
    line = '{key}={value}\n'.format(key=key, value=value)
    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(line)
    sys.stdout.write(line)

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


def extract_version(filename):
    """Extract version from a filename.
    Return the substring between the last '@' and last '.'"""
    s = os.path.basename(filename)
    return s[s.rfind('@')+1:s.rfind('.')]


def format_package(namespace, name, version):
    """Canonical package representation in namespace:name@version format"""
    if version:
        return "{}:{}@{}".format(namespace, name, version)
    else:
        return "{}:{}".format(namespace, name)


def parse_package(package):
    """Parse a package string.

    The following forms are supported:
        namespace:name
        namespace:name@version
        namespace/name
        namespace/name@version

    Returns a tuple (namespace, name, version)
    """
    left, version = package, None
    if '@' in package:
        left, version = package.split('@', 1)
    if ':' in left:
        namespace, name = left.split(':', 1)
    elif '/' in left:
        namespace, name = left.split('/', 1)
    else:
        namespace, name = None, left

    if not namespace:
        raise ValueError("package namespace is required")
    if not name:
        raise ValueError("package version is required")

    if not re.match(r"[\w-]+", namespace):
        raise ValueError("invalid package namespace")
    if not re.match(r"[\w-]+", name):
        raise ValueError("invalid package name")
    if version:
        # throws on failed validation
        semver.Version.parse(version)
    return namespace, name, version
