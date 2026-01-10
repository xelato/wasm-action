import os
import tempfile
import unittest

from wasm_action.action import push
from wasm_action.util import get_github_outputs

from helpers import use_cassette

class TestWargPush(unittest.TestCase):

    @use_cassette('test/vcr/action-push-warg-already-released.yaml')
    def test_warg_push_already_released(self):
        os.environ['GITHUB_OUTPUT'] = tempfile.mktemp()
        try:
            push(args=[
                "--registry", "wa.dev",
                "--package", 'rocketniko:gcd@0.0.2',
                "--path", "test/files/gcd.wasm",
            ])
        except SystemExit as e:
            self.assertEqual(e.code, 1)
            outputs = get_github_outputs()
            self.assertEqual(outputs['error'], 'an entry attempted to release version 0.0.2 which is already released')

        else:
            assert False, "did not exit"

    @use_cassette('test/vcr/action-push-warg-same-source.yaml')
    def test_warg_push_already_released(self):
        os.environ['GITHUB_OUTPUT'] = tempfile.mktemp()
        try:
            push(args=[
                "--registry", "wa.dev",
                "--package", 'rocketniko:gcd@0.0.3',
                "--path", "test/files/gcd.wasm",
            ])
        except SystemExit as e:
            self.assertEqual(e.code, 0)
            outputs = get_github_outputs()
            self.assertEqual(outputs['state'], 'published')
            self.assertEqual(outputs['package'], 'rocketniko:gcd@0.0.3')
            self.assertEqual(outputs['package-namespace'], 'rocketniko')
            self.assertEqual(outputs['package-name'], 'gcd')
            self.assertEqual(outputs['package-version'], '0.0.3')
            self.assertEqual(outputs['package-record-id'], 'sha256:aba3083af805a794b8075361d760db16d1701e32fe1b7713f3ec9996a81adaeb')

        else:
            assert False, "did not exit"
