import scripts.repocompiler as repocompiler
import scripts.pageparser as pageparser


def samples_run_without_errors():
    sample_repos = pageparser.compile_sample_repos()
    run_results = repocompiler.run_repos(sample_repos)
    return run_results and False not in run_results


def samples_are_free_of_lints():
    sample_repos = pageparser.compile_sample_repos()
    return False
