import unittest
import os
import scripts.repocompiler as repocompiler
import scripts.pageparser as pageparser


CLONE_BENCH_FOLDER = 'testbench'


class SamplesFunctionalTest(unittest.TestCase):
    sample_code_folders = []

    @classmethod
    def setUpClass(cls):
        sample_repos = pageparser.compile_sample_repos()
        os.chdir('integrate')
        for sample in sample_repos:
            cloned_folder = repocompiler.clone_sample_to_folder(CLONE_BENCH_FOLDER, sample)
            SamplesFunctionalTest.sample_code_folders.append(cloned_folder)

    def test_samples_are_free_of_lints(self):
        run_results = repocompiler.lint_folders(SamplesFunctionalTest.sample_code_folders)
        self.assertTrue(run_results and False not in run_results)

    def test_samples_will_run(self):
        run_results = \
            repocompiler.run_module_in_cloned_folders(SamplesFunctionalTest.sample_code_folders)
        self.assertTrue(run_results and False not in run_results)

    @classmethod
    def tearDownClass(cls):
        repocompiler.remove_tree(CLONE_BENCH_FOLDER)
        os.chdir('..')


if __name__ == '__main__':
    unittest.main()
