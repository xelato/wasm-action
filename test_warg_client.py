import unittest

from warg_crypto import PrivateKey, PublicKey
from warg_client import WargClient, generate_log_id


class TestWargClient(unittest.TestCase):

    def test_generate_log_id(self):
        log_id = generate_log_id(namespace='wasi', name='io')
        self.assertEqual(log_id, "sha256:4dd80f8165e12905a35accf700f015164b844127ab341a8860f4769d319cc8ab")
