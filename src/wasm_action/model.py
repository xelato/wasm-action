
import enum
from dataclasses import dataclass


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


@dataclass
class PackageDownload:
    namespace: str
    name: str
    version: str
    content: bytes
    digest: str


@dataclass
class PackageRecord:
    id: str
    prev_id: str
    proto: object
    orig: object
