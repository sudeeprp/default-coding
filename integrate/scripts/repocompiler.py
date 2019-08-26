import os
import stat
import importlib
import inspect
from git import Repo


def remove_tree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


def clone_sample(sample):
    url_to_clone = 'https://gist.github.com/{}.git'.format(sample)
    target_dirname = os.path.join('testbench', sample)
    remove_tree(target_dirname)
    Repo.clone_from(url_to_clone, target_dirname)
    return target_dirname


def try_calling(function):
    try:
        function()
    except AssertionError:
        return False
    else:
        return True


def run_tests(funcs_list):
    test_results = []
    for function_tuple in funcs_list:
        if function_tuple[0].startswith('test_'):
            test_results.append(try_calling(function_tuple[1]))
    return test_results


def run_sample(module_name_of_sample_code):
    try:
        module_with_sample_code = importlib.import_module(module_name_of_sample_code)
    except ModuleNotFoundError:
        return False
    except SyntaxError:
        return False
    else:
        funcs_in_sample = inspect.getmembers(module_with_sample_code, inspect.isfunction)
        return False not in run_tests(funcs_in_sample)


def run_repos(sample_repos):
    run_results = []
    for sample in sample_repos:
        folder = clone_sample(sample)
        module_name_of_sample_code = module_name_from_sample()
        run_results.append(run_sample(module_name_of_sample_code))
    return run_results
