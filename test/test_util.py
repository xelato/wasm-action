import unittest
import datetime
from wasm_action.util import parse_package, CalVer


class TestUtil(unittest.TestCase):

    def test_parse_package(self):
        self.assertEqual(parse_package('wasi:io'), ('wasi', 'io', None))
        self.assertEqual(parse_package('wasi/io'), ('wasi', 'io', None))
        self.assertEqual(parse_package('wasi:io@0.1.0'), ('wasi', 'io', '0.1.0'))
        self.assertEqual(parse_package('wasi/io@0.1.0'), ('wasi', 'io', '0.1.0'))
        # calendar versioning
        parse_package('foo:bar@YY.MM.DD')

    def test_calver(self):
        then = datetime.datetime(year=2006, month=2, day=6)
        for pattern, version in {
                "1.2.3": "1.2.3",
                "YYYY.MM.DD": "2006.2.6",
                "YYYY.YY.0Y.MM.0M.WW.0W.DD.0D": '2006.6.06.2.02.6.06.6.06',
            }.items():

            # eval for current date
            CalVer(pattern).version()

            # eval for specific date
            self.assertEqual(CalVer(pattern).version(at=then), version)
