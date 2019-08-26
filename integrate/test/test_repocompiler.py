import unittest
import os
import scripts.repocompiler as repocompiler


class RepoCompilerTester(unittest.TestCase):
    def test_clone_brings_folder_to_testbench(self):
        folder = repocompiler.clone_sample('06eb7daec8c080bbc4ec3b7b6f3d9bfe')
        self.assertTrue(os.path.exists(folder))

    def test_failure_reported_when_sample_asserts(self):
        self.assertFalse(repocompiler.run_sample('samples.sample_fails'))
        self.assertFalse(repocompiler.run_sample('samples.sample_norun'))
        self.assertTrue(repocompiler.run_sample('samples.sample_passes'))


if __name__ == '__main__':
    unittest.main()
