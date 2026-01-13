
import importlib.metadata
__version__ = importlib.metadata.version("wasm_action")

from .lib import push, pull
