import unittest
import importlib
import scripts.repocompiler as repocompiler


class RepoCompilerTester(unittest.TestCase):
    def test_clone_brings_module_into_testbench(self):
        repo_folder = repocompiler.clone_sample_to_folder\
            (repocompiler.CLONE_BENCH_FOLDER, '06eb7daec8c080bbc4ec3b7b6f3d9bfe')
        module_name = repocompiler.py_module_in_folder(repo_folder)
        self.assertIsNotNone(importlib.import_module(module_name))

    def test_failure_reported_when_sample_asserts(self):
        self.assertFalse(repocompiler.run_sample('test.test_samples.sample_fails'))
        self.assertFalse(repocompiler.run_sample('test.test_samples.sample_norun'))
        self.assertTrue(repocompiler.run_sample('test.test_samples.sample_passes'))
        self.assertFalse(repocompiler.run_sample('test.test_samples.sample_hasnotest'))


if __name__ == '__main__':
    unittest.main()
