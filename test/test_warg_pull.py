import os
import tempfile
import unittest

from wasm_action.cli import pull
from wasm_action.util import get_github_outputs

from helpers import use_cassette


class TestWargPull(unittest.TestCase):
    @use_cassette("test/vcr/action-pull-warg.yaml")
    def test_warg_pull(self):
        os.environ["GITHUB_OUTPUT"] = tempfile.mktemp()
        try:
            pull(
                args=[
                    "--registry",
                    "wa.dev",
                    "--package",
                    "wasi/io",
                ]
            )
        except SystemExit as e:
            self.assertEqual(e.code, 0)
            outputs = get_github_outputs()
            self.assertEqual(outputs["registry"], "wa.dev")
            self.assertEqual(outputs["registry-type"], "warg")
            self.assertEqual(outputs["warg-url"], "https://warg.wa.dev")
            self.assertEqual(outputs["package"], "wasi:io@0.2.0")
            self.assertEqual(outputs["package-namespace"], "wasi")
            self.assertEqual(outputs["package-name"], "io")
            self.assertEqual(outputs["package-version"], "0.2.0")
            self.assertEqual(
                outputs["digest"],
                "sha256:c33b1dbf050f64229ff4decbf9a3d3420e0643a86f5f0cea29f81054820020a6",
            )
            self.assertEqual(outputs["filename"], "wasi:io@0.2.0.wasm")
            self.assertTrue(os.path.exists(outputs["filename"]))
            self.assertTrue(os.path.isfile(outputs["filename"]))
            os.remove(outputs["filename"])
        else:
            assert False, "did not exit"
