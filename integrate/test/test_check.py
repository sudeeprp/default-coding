import unittest
import scripts.check as checker


class CheckTester(unittest.TestCase):
    def test_defaults_are_checked_ok(self):
        self.assertTrue(checker.check_defaults())


if __name__ == '__main__':
    unittest.main()
