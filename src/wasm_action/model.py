
import enum
from collections import namedtuple


class Action(enum.Enum):
    PUSH = 'push'
    PULL = 'pull'

    def __str__(self):
        return self.value


class RegistryType(enum.Enum):
    OCI = 'oci'
    WARG = 'warg'

    def __str__(self):
        return self.value


PackageDownload = namedtuple('PackageDownload', (
    'namespace',
    'name',
    'version',
    'content',
    'digest',
    ))
