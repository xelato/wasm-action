
"""
Cryptography support for interacting with warg-server.

Warg uses ECC secp256r1 for signing content uploads.

Implementation relies on cryptography package (using OpenSSL internally).

"""

import base64
import hashlib

from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
)


class PrivateKey:

    CURVES = {
        'ecdsa-p256': ec.SECP256R1(),
    }

    @classmethod
    def generate(cls) -> ec.EllipticCurvePrivateKey:
        """Generate a new private key"""
        return cls(ec.generate_private_key(curve=ec.SECP256R1()))

    @classmethod
    def load(cls, text: str):
        """
        Decode a key in `<algo>:<base64>` format.
        """
        if ':' not in text:
            raise ValueError('required format: <algo>:<base64>')

        algo, key_b64 = text.split(':', 1)

        curve = cls.CURVES.get(algo)
        if not curve:
            raise ValueError('algorithm not supported: {}'.format(algo))

        key_bytes = base64.b64decode(key_b64)
        # todo: compare bytes length with curve key length

        key_int = int.from_bytes(key_bytes, byteorder='big')
        key = ec.derive_private_key(key_int, curve=curve)
        return cls(key)

    def __init__(self, key: ec.EllipticCurvePrivateKey):
        self.key = key

    def sign(self, data):
        """Generate signature"""
        return self.key.sign(data, signature_algorithm=ec.ECDSA(hashes.SHA256()))

    def sign_canonical(self, data):
        """Generate signature in canonical format"""
        return "{}:{}".format('ecdsa-p256', base64.b64encode(self.sign(data)).decode('ascii'))

    def public_key(self):
        return PublicKey(self.key.public_key())

    def pem_pkcs8(self):
        res = self.key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
        return res.decode('ascii')

    def pem_openssl(self):
        res = self.key.private_bytes(Encoding.PEM, PrivateFormat.TraditionalOpenSSL, NoEncryption())
        return res.decode('ascii')

    def der_pkcs8(self):
        return self.key.private_bytes(Encoding.DER, PrivateFormat.PKCS8, NoEncryption())

    def der_openssl(self):
        return self.key.private_bytes(Encoding.DER, PrivateFormat.TraditionalOpenSSL, NoEncryption())

    def canonical(self):
        """Convert to `<algo>:<base64>` format."""
        key_int = self.key.private_numbers().private_value
        key_bytes = key_int.to_bytes(length=32, byteorder='big')
        key_b64 = base64.b64encode(key_bytes).decode('ascii')
        return "{}:{}".format('ecdsa-p256', key_b64)


class PublicKey:

    def __init__(self, key: ec.EllipticCurvePublicKey):
        self.key = key

    def verify(self, signature, data):
        """Verify signature"""
        try:
            self.key.verify(signature=signature, data=data, signature_algorithm=ec.ECDSA(hashes.SHA256()))
        except exceptions.InvalidSignature:
            return False
        else:
            return True

    @property
    def public_numbers(self):
        return self.key.public_numbers()

    def pem(self):
        res = self.key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
        return res.decode('ascii')

    def der(self):
        return self.key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

    def ssh(self):
        res = self.key.public_bytes(Encoding.OpenSSH, PublicFormat.OpenSSH)
        return res.decode('ascii')

    def x962_compressed_point(self):
        return self.key.public_bytes(Encoding.X962, PublicFormat.CompressedPoint)

    def x962_uncompressed_point(self):
        return self.key.public_bytes(Encoding.X962, PublicFormat.UncompressedPoint)

    def canonical(self):
        """Convert to `<algo>:<base64>` format."""
        key_bytes = self.x962_compressed_point()
        key_b64 = base64.b64encode(key_bytes).decode('ascii')
        return "{}:{}".format('ecdsa-p256', key_b64)

    def fingerprint(self):
        """Used as Key ID"""
        return "sha256:{}".format(hashlib.sha256(self.canonical().encode('ascii')).hexdigest())
