import unittest

from wasm_action.warg.crypto import PrivateKey, PublicKey


class TestKeys(unittest.TestCase):

    def test_private_key(self):
        k1 = PrivateKey.generate()
        k2 = PrivateKey.load(k1.canonical())
        self.assertEqual(k1.canonical(), k2.canonical())

    def test_basic(self):
        key = PrivateKey.load("ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk=")
        self.assertEqual(key.canonical(), "ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk=")
        self.assertEqual(key.public_key().canonical(), "ecdsa-p256:A1OfZz5Y9Ny7VKPVwroCTQPAr9tmlI4U/UTYHZHA87AF")
        self.assertEqual(key.public_key().fingerprint(), "sha256:d6d9b4cd077a829c0275233bf3843c8294e250dfcc82b8ea15745e92982a820d")

    def test_sign(self):
        private_key = PrivateKey.generate()
        public_key = private_key.public_key()

        data = b"Hello, WebAssembly!"
        signature = private_key.sign(data)
        ok = public_key.verify(signature, data)
        self.assertTrue(ok)

    def test_private_key_formats(self):
        key = PrivateKey.load("ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk=")
        self.assertEqual(key.canonical(), "ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk=")
        self.assertEqual(key.pem_pkcs8().strip(), """
-----BEGIN PRIVATE KEY-----
MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgI+UlDo0HxyBBFeel
hPPWmD+LnklOpqZDkrFP5VduASmhRANCAARTn2c+WPTcu1Sj1cK6Ak0DwK/bZpSO
FP1E2B2RwPOwBa3h1LGUdhv9/HHDx39tHCTgY9BdLI29qgOkWt6+zRjz
-----END PRIVATE KEY-----
""".strip())

        self.assertEqual(key.pem_openssl().strip(), """
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEICPlJQ6NB8cgQRXnpYTz1pg/i55JTqamQ5KxT+VXbgEpoAoGCCqGSM49
AwEHoUQDQgAEU59nPlj03LtUo9XCugJNA8Cv22aUjhT9RNgdkcDzsAWt4dSxlHYb
/fxxw8d/bRwk4GPQXSyNvaoDpFrevs0Y8w==
-----END EC PRIVATE KEY-----
""".strip())

        self.assertEqual(key.der_pkcs8(), b'0\x81\x87\x02\x01\x000\x13\x06\x07*\x86H\xce=\x02\x01\x06\x08*\x86H\xce=\x03\x01\x07\x04m0k\x02\x01\x01\x04 #\xe5%\x0e\x8d\x07\xc7 A\x15\xe7\xa5\x84\xf3\xd6\x98?\x8b\x9eIN\xa6\xa6C\x92\xb1O\xe5Wn\x01)\xa1D\x03B\x00\x04S\x9fg>X\xf4\xdc\xbbT\xa3\xd5\xc2\xba\x02M\x03\xc0\xaf\xdbf\x94\x8e\x14\xfdD\xd8\x1d\x91\xc0\xf3\xb0\x05\xad\xe1\xd4\xb1\x94v\x1b\xfd\xfcq\xc3\xc7\x7fm\x1c$\xe0c\xd0],\x8d\xbd\xaa\x03\xa4Z\xde\xbe\xcd\x18\xf3')
        self.assertEqual(key.der_openssl(), b'0w\x02\x01\x01\x04 #\xe5%\x0e\x8d\x07\xc7 A\x15\xe7\xa5\x84\xf3\xd6\x98?\x8b\x9eIN\xa6\xa6C\x92\xb1O\xe5Wn\x01)\xa0\n\x06\x08*\x86H\xce=\x03\x01\x07\xa1D\x03B\x00\x04S\x9fg>X\xf4\xdc\xbbT\xa3\xd5\xc2\xba\x02M\x03\xc0\xaf\xdbf\x94\x8e\x14\xfdD\xd8\x1d\x91\xc0\xf3\xb0\x05\xad\xe1\xd4\xb1\x94v\x1b\xfd\xfcq\xc3\xc7\x7fm\x1c$\xe0c\xd0],\x8d\xbd\xaa\x03\xa4Z\xde\xbe\xcd\x18\xf3')

    def test_public_key_formats(self):
        key = PrivateKey.load(
            "ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk="
        ).public_key()

        self.assertEqual(key.canonical(), "ecdsa-p256:A1OfZz5Y9Ny7VKPVwroCTQPAr9tmlI4U/UTYHZHA87AF")
        self.assertEqual(key.fingerprint(), "sha256:d6d9b4cd077a829c0275233bf3843c8294e250dfcc82b8ea15745e92982a820d")

        self.assertEqual(key.pem().strip(), """
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEU59nPlj03LtUo9XCugJNA8Cv22aU
jhT9RNgdkcDzsAWt4dSxlHYb/fxxw8d/bRwk4GPQXSyNvaoDpFrevs0Y8w==
-----END PUBLIC KEY-----
""".strip())

        self.assertEqual(key.der(), b'0Y0\x13\x06\x07*\x86H\xce=\x02\x01\x06\x08*\x86H\xce=\x03\x01\x07\x03B\x00\x04S\x9fg>X\xf4\xdc\xbbT\xa3\xd5\xc2\xba\x02M\x03\xc0\xaf\xdbf\x94\x8e\x14\xfdD\xd8\x1d\x91\xc0\xf3\xb0\x05\xad\xe1\xd4\xb1\x94v\x1b\xfd\xfcq\xc3\xc7\x7fm\x1c$\xe0c\xd0],\x8d\xbd\xaa\x03\xa4Z\xde\xbe\xcd\x18\xf3')
        self.assertEqual(key.ssh(), "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFOfZz5Y9Ny7VKPVwroCTQPAr9tmlI4U/UTYHZHA87AFreHUsZR2G/38ccPHf20cJOBj0F0sjb2qA6Ra3r7NGPM=")

        self.assertEqual(key.x962_compressed_point(), b'\x03S\x9fg>X\xf4\xdc\xbbT\xa3\xd5\xc2\xba\x02M\x03\xc0\xaf\xdbf\x94\x8e\x14\xfdD\xd8\x1d\x91\xc0\xf3\xb0\x05')
        self.assertEqual(key.x962_uncompressed_point(), b'\x04S\x9fg>X\xf4\xdc\xbbT\xa3\xd5\xc2\xba\x02M\x03\xc0\xaf\xdbf\x94\x8e\x14\xfdD\xd8\x1d\x91\xc0\xf3\xb0\x05\xad\xe1\xd4\xb1\x94v\x1b\xfd\xfcq\xc3\xc7\x7fm\x1c$\xe0c\xd0],\x8d\xbd\xaa\x03\xa4Z\xde\xbe\xcd\x18\xf3')
