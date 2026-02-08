import unittest
from helpers import use_cassette

from wasm_action.warg.client import WargClient, generate_log_id
from wasm_action.warg.actions import warg_pull


class TestWargClient(unittest.TestCase):
    def setUp(self):
        self.client = WargClient(
            registry="wa.dev",
            warg_url="https://warg.wa.dev",
        )

    def test_generate_log_id(self):
        log_id = generate_log_id(namespace="wasi", name="io")
        self.assertEqual(
            log_id,
            "sha256:4dd80f8165e12905a35accf700f015164b844127ab341a8860f4769d319cc8ab",
        )

    @use_cassette("test/vcr/warg-client.yaml")
    def test_client(self):
        namespace = "wasi"
        name = "io"
        res = self.client.get_warg_registry(namespace)
        self.assertEqual(res, "wasi.wa.dev")

        res = self.client.get_checkpoint(namespace=namespace)
        res = self.client.fetch_logs(
            namespace=namespace, name=name, log_length=res.contents.log_length
        )
        assert res is not None

        res = self.client.fetch_names(namespace, name)
        assert res is not None

    @use_cassette("test/vcr/warg-pull.yaml")
    def test_warg_pull(self):
        download = warg_pull(
            registry="wa.dev",
            warg_url="https://warg.wa.dev",
            namespace="wasi",
            name="io",
            version=None,
        )
        assert download.namespace == "wasi"
        assert download.name == "io"
        assert download.version == "0.2.0"
        assert (
            download.digest
            == "sha256:c33b1dbf050f64229ff4decbf9a3d3420e0643a86f5f0cea29f81054820020a6"
        )
        assert download.content is not None
