
import os
import re
import sys
import datetime
import functools
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
        # evaluate any calver specifiers
        version = CalVer(version).version()
        # throws on failed validation
        semver.Version.parse(version)
    return namespace, name, version


class CalVer:
    """Calendar Versioning according to https://calver.org (zero-padded formats excluded)"""

    SPEC = {
        'YYYY': lambda d: str(d.year),
        'YY': lambda d: str(d.year % 100),
        'MM': lambda d: str(d.month),
        'WW': lambda d: str(d.isocalendar().week),
        'DD': lambda d: str(d.day),
    }

    def __init__(self, pattern):
        self.pattern = pattern

    def now(self) -> datetime.datetime:
        if not hasattr(datetime, 'UTC'):
            # 3.10
            return datetime.datetime.utcnow()
        return datetime.datetime.now(datetime.UTC)

    def version(self, at: datetime.datetime=None):
        when = at or self.now()
        return ".".join([
            self.SPEC[part.upper()](when)
            if part.upper() in self.SPEC else part
            for part in self.pattern.split('.')
        ])


class cli_error_handler(object):
    """Decorator for CLI error handling"""

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            # print error and return 1
            sys.exit(e)
