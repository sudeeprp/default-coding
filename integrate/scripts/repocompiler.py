import os
import stat
import importlib
import inspect
from git import Repo


CLONE_BENCH_FOLDER = 'testbench'


def remove_tree(top):
    if os.path.isdir(top):
        for root, dirs, files in os.walk(top, topdown=False):
            for name in files:
                filename = os.path.join(root, name)
                os.chmod(filename, stat.S_IWUSR)
                os.remove(filename)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(top)


def py_module_in_folder(folder_name):
    pyfiles = filter(lambda name: name.endswith('.py'), os.listdir(folder_name))
    return folder_name.replace(os.sep, '.') + '.' + next(pyfiles, None).replace('.py', '')


def clone_sample_to_folder(clone_base_folder, sample):
    url_to_clone = 'https://gist.github.com/{}.git'.format(sample)
    target_dirname = os.path.join(clone_base_folder, sample)
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
        print('Module not found: ' + module_name_of_sample_code)
        return False
    except SyntaxError:
        print('Syntax error in module: ' + module_name_of_sample_code)
        return False
    else:
        funcs_in_sample = inspect.getmembers(module_with_sample_code, inspect.isfunction)
        test_results = run_tests(funcs_in_sample)
        if not test_results:
            print("No tests in " + module_name_of_sample_code)
        return test_results and False not in test_results


def run_module_in_cloned_folders(sample_folders):
    run_results = []
    for repo_folder in sample_folders:
        module_name_of_sample_code = py_module_in_folder(repo_folder)
        run_results.append(run_sample(module_name_of_sample_code))
    return run_results


def lint_sample(folder_of_sample_code):
    from pylint import epylint as lint
    pylintrc_path = os.path.realpath('.pylintrc')
    out, err = lint.py_run(folder_of_sample_code + ' --rcfile='+ pylintrc_path, return_std=True)
    console_out = out.read()
    success = 'rated at 10.00/10' in console_out
    if not success:
        print(console_out + '\n' + err.read())
    return success


def lint_folders(sample_folders):
    run_results = []
    for folder in sample_folders:
        run_results.append(lint_sample(folder))
    return run_results
