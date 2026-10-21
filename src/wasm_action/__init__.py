import importlib.metadata

try:
    __version__ = importlib.metadata.version("wasm-action")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

from .lib import pull as pull
from .lib import push as push
