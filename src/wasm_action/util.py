
import os
import re
import sys
import requests
import semver


def add_github_output(key, value):
    """Add a github job output to the file pointed by the GITHUB_OUTPUT variable"""
    line = '{key}={value}\n'.format(key=key, value=value)
    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(line)
    sys.stdout.write(line)

def get_github_outputs():
    if 'GITHUB_OUTPUT' not in os.environ:
        return {}
    with open(os.environ['GITHUB_OUTPUT'], 'r') as f:
        content = f.read()
    result = {}
    for line in [line.strip() for line in content.split('\n')]:
        if not line:
            continue
        key, value = line.split('=', 1)
        result[key] = value
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
