'''
This is a sample that passes linting but fails one test
'''

import json


def dummy_function():
    return []


def test_passes():
    json.loads('{}')
    assert True


def test_fails():
    assert False


if __name__ == '__main__':
    test_passes()
    test_fails()
