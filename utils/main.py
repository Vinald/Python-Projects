from timeit import default_timer as timer
from textwrap import dedent
import math


def _str_trunc(data, size=100):
    data_str = str(data)
    if len(data_str) > size + 3:
        return data_str[:size] + '...'
    return data_str


def _show_test_case(test_case):
    inputs = test_case['input']

    if 'outputs' in test_case:
        expected_text = "Outputs"
        expected = test_case.get('outputs')
    else:
        expected_text = "Output"
        expected = test_case.get('output')

    print(dedent("""
    Input:
    {}

    Expected {}:
    {}
    """.format(_str_trunc(inputs), expected_text, _str_trunc(expected))))


def _show_result(result):
    actual_output, passed, runtime = result
    message = "\033[92mPASSED\033[0m" if passed else "\033[91mFAILED\033[0m"
    print(dedent("""
    Actual Output:
    {}

    Execution Time:
    {} ms

    Test Result:
    {}
    """.format(_str_trunc(actual_output), runtime, message)))


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1