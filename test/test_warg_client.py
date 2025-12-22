import unittest
import vcr

from wasm_action.warg_client import WargClient, generate_log_id


class TestWargClient(unittest.TestCase):

    def setUp(self):
        self.client = WargClient(
            registry="wa.dev",
            warg_url="https://warg.wa.dev",
        )

    def test_generate_log_id(self):
        log_id = generate_log_id(namespace='wasi', name='io')
        self.assertEqual(log_id, "sha256:4dd80f8165e12905a35accf700f015164b844127ab341a8860f4769d319cc8ab")

    @vcr.use_cassette('test/vcr/warg-client.yaml')
    def test_client(self):
        namespace = 'wasi'
        name = 'io'
        res = self.client.get_warg_registry(namespace)
        self.assertEqual(res, 'wasi.wa.dev')

        res = self.client.get_checkpoint(namespace=namespace)
        res = self.client.fetch_logs(
            namespace=namespace, name=name, log_length=res.contents.log_length)
        assert res is not None
