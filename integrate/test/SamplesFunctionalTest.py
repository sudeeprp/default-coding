import unittest
import scripts.checksamples as samples_check


class SamplesFunctionalTest(unittest.TestCase):
    def test_samples_are_free_of_lints(self):
        self.assertTrue(samples_check.samples_are_free_of_lints())

    def test_samples_will_run(self):
        self.assertTrue(samples_check.samples_run_without_errors())


if __name__ == '__main__':
    unittest.main()
