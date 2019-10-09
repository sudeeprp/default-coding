import scripts.repocompiler as repocompiler
import scripts.pageparser as pageparser


def check_samples():
    sample_repos = pageparser.compile_sample_repos()
    run_results = repocompiler.run_repos(sample_repos)
    return run_results and False not in run_results
