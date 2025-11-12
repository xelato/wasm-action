import unittest

from wasm_action.util import parse_package


class TestUtil(unittest.TestCase):

    def test_parse_package(self):
        self.assertEqual(parse_package('wasi:io'), ('wasi', 'io', None))
        self.assertEqual(parse_package('wasi/io'), ('wasi', 'io', None))
        self.assertEqual(parse_package('wasi:io@0.1.0'), ('wasi', 'io', '0.1.0'))
        self.assertEqual(parse_package('wasi/io@0.1.0'), ('wasi', 'io', '0.1.0'))
