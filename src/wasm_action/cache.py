
import os
import hashlib

CACHE = os.path.join(os.environ['HOME'], '.cache', 'wasm-action')


def fetch(content_hash: str) -> bytes:
    """Fetch object from cache"""
    if not os.path.exists(CACHE):
        os.makedirs(CACHE)

    filename = os.path.join(CACHE, content_hash)
    if not os.path.exists(filename):
        return None

    with open(filename, 'rb') as f:
        content = f.read()

    computed_hash = hashlib.sha256(content).hexdigest()
    if computed_hash != content_hash:
        raise ValueError('content with hash has been tempered: {}'.format(content_hash))
    return content


def store(content: bytes):
    """Store object in cache"""
    if not os.path.exists(CACHE):
        os.makedirs(CACHE)

    content_hash = hashlib.sha256(content).hexdigest()
    filename = os.path.join(CACHE, content_hash)
    with open(filename, 'wb') as f:
        f.write(content)


def exists(content_hash: str) -> bool:
    """Check if object exists"""
    if not os.path.exists(CACHE):
        os.makedirs(CACHE)

    filename = os.path.join(CACHE, content_hash)
    return os.path.exists(filename)


def compute_hash(content: bytes) -> str:
    """Compute hash without storing the object"""
    return hashlib.sha256(content).hexdigest()


def size(content_hash: str) -> int:
    """Return size of stored object"""
    if not os.path.exists(CACHE):
        os.makedirs(CACHE)
    filename = os.path.join(CACHE, content_hash)
    if not os.path.exists(filename):
        return 0
    return os.stat(filename).st_size
