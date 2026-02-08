import os
import tempfile
import unittest

from wasm_action.cli import push
from wasm_action.util import get_github_outputs

from helpers import use_cassette

DUMMY_PRIVATE_KEY = "ecdsa-p256:I+UlDo0HxyBBFeelhPPWmD+LnklOpqZDkrFP5VduASk="


class TestWargPush(unittest.TestCase):
    @use_cassette("test/vcr/action-push-warg-already-released.yaml")
    def test_warg_push_already_released(self):
        os.environ["GITHUB_OUTPUT"] = tempfile.mktemp()
        os.environ["WARG_PRIVATE_KEY"] = DUMMY_PRIVATE_KEY
        try:
            push(
                args=[
                    "--registry",
                    "wa.dev",
                    "--package",
                    "rocketniko:gcd@0.0.2",
                    "--path",
                    "test/files/gcd.wasm",
                ]
            )
        except SystemExit as e:
            self.assertEqual(e.code, 1)
            outputs = get_github_outputs()
            self.assertEqual(
                outputs["error"],
                "an entry attempted to release version 0.0.2 which is already released",
            )

        else:
            assert False, "did not exit"

    @use_cassette("test/vcr/action-push-warg-same-source.yaml")
    def test_warg_push_already_released_same_source(self):
        os.environ["GITHUB_OUTPUT"] = tempfile.mktemp()
        os.environ["WARG_PRIVATE_KEY"] = DUMMY_PRIVATE_KEY
        try:
            push(
                args=[
                    "--registry",
                    "wa.dev",
                    "--package",
                    "rocketniko:gcd@0.0.3",
                    "--path",
                    "test/files/gcd.wasm",
                ]
            )
        except SystemExit as e:
            self.assertEqual(e.code, 0)
            outputs = get_github_outputs()
            self.assertEqual(outputs["state"], "published")
            self.assertEqual(outputs["package"], "rocketniko:gcd@0.0.3")
            self.assertEqual(outputs["package-namespace"], "rocketniko")
            self.assertEqual(outputs["package-name"], "gcd")
            self.assertEqual(outputs["package-version"], "0.0.3")
            self.assertEqual(
                outputs["package-record-id"],
                "sha256:aba3083af805a794b8075361d760db16d1701e32fe1b7713f3ec9996a81adaeb",
            )

        else:
            assert False, "did not exit"

    @use_cassette("test/vcr/action-push-warg-upload-source.yaml")
    def test_warg_push_new_version(self):
        os.environ["GITHUB_OUTPUT"] = tempfile.mktemp()
        os.environ["WARG_PRIVATE_KEY"] = DUMMY_PRIVATE_KEY
        try:
            push(
                args=[
                    "--registry",
                    "wa.dev",
                    "--package",
                    "rocketniko:gcd@0.0.6",
                    "--path",
                    "test/files/gcd.wasm",
                ]
            )
        except SystemExit as e:
            self.assertEqual(e.code, 0)
            outputs = get_github_outputs()
            self.assertEqual(outputs["state"], "published")
            self.assertEqual(outputs["package"], "rocketniko:gcd@0.0.6")
            self.assertEqual(outputs["package-namespace"], "rocketniko")
            self.assertEqual(outputs["package-name"], "gcd")
            self.assertEqual(outputs["package-version"], "0.0.6")
            self.assertEqual(
                outputs["package-record-id"],
                "sha256:b28e3de828e6680c0d6e8fc8bca44b7475f02de59cbd90245e251a0bd4992715",
            )

        else:
            assert False, "did not exit"
