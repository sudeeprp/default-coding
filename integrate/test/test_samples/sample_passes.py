'''
This is a sample that passes linting and tests
'''
import json


def dummy_function():
    return []


def test_passes():
    json.loads('{}')
    assert True


if __name__ == '__main__':
    test_passes()
