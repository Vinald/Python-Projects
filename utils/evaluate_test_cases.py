from timeit import default_timer as timer
from utils.main import _show_test_case,  _show_result
from utils.evaluate_test_case import evaluate_test_case

import math


def evaluate_test_cases(function, test_cases, error_only=False, summary_only=False):
    results = []
    for i, test_case in enumerate(test_cases):
        if not error_only:
            print("\n\033[1mTEST CASE #{}\033[0m".format(i))
        result = evaluate_test_case(function, test_case, display=False)
        results.append(result)
        if error_only and not result[1]:
            print("\n\033[1mTEST CASE #{}\033[0m".format(i))
        if not error_only or not result[1]:
            _show_test_case(test_case)
            _show_result(result)

    total = len(results)
    num_passed = sum([r[1] for r in results])
    print("\n\033[1mSUMMARY\033[0m")
    print("\nTOTAL: {}, \033[92mPASSED\033[0m: {}, \033[91mFAILED\033[0m: {}".format(
        total, num_passed, total - num_passed))
    return results
