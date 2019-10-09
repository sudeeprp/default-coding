import unittest
import scripts.checksamples as checker


class SamplesFunctionalTest(unittest.TestCase):
    def test_samples_are_ok(self):
        self.assertTrue(checker.check_samples())


if __name__ == '__main__':
    unittest.main()
