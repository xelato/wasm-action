
import importlib.metadata

try:
	__version__ = importlib.metadata.version("wasm-action")
except importlib.metadata.PackageNotFoundError:
	__version__ = "0.0.0"

from .lib import push, pull
