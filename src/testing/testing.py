"""
This module provides functionality to run unit tests with setup and teardown phases.
It includes a simple sign function and corresponding test cases, as well as a test runner
that can execute tests based on a given pattern.

Functions:
- sign(value): Returns the sign of a given number.
- test_sign_negative(): Tests the sign function with a negative value.
- test_sign_positive(): Tests the sign function with a positive value.
- test_sign_zero(): Tests the sign function with zero.
- test_sign_error(): Tests the sign function with an intentional error.
- setup_tests(): Prints a setup message before tests.
- teardown_tests(): Prints a teardown message after tests.
- find_func(prefix): Finds a function by its prefix in the global namespace.
- run_tests(pattern): Runs tests that match the given pattern.
"""

import time
import sys


def sign(value):
    """
    Returns the sign of a given number.

    :param value: The number to check.
    :type value: int or float
    :return: -1 if the number is negative, 1 if positive, and 0 if zero.
    :rtype: int
    """
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0


def test_sign_negative():
    """Tests the sign function with a negative value."""
    assert sign(-3) == -1


def test_sign_positive():
    """Tests the sign function with a positive value."""
    assert sign(3) == 1


def test_sign_zero():
    """Tests the sign function with zero."""
    assert sign(0) == 0


def test_sign_error():
    """Tests the sign function with an intentional error."""
    assert sign(-3) == -1


def setup_tests():
    """Prints a setup message before tests."""
    print("Setting up before tests")


def teardown_tests():
    """Prints a teardown message after tests."""
    print("Teardown after tests")


def find_func(prefix):
    """
    Finds a function by its prefix in the global namespace.

    :param prefix: The prefix to search for.
    :type prefix: str
    :return: The first function found with the given prefix, or None if not found.
    :rtype: function or None
    """
    for name, func in globals().items():
        if name.startswith(prefix):
            return func
    return None


def run_tests(pattern):
    """
    Runs tests that match the given pattern.

    :param pattern: The pattern to match test names against.
    :type pattern: str, optional
    """
    results = {
        "pass": [],
        "fail": [],
        "error": []
    }

    setup_func = find_func("setup_")
    teardown_func = find_func("teardown_")

    for name, test in globals().items():
        if not name.startswith("test_"):
            continue
        if pattern and pattern not in name:
            continue
        try:
            if setup_func:
                setup_func()
            start = time.time()
            if callable(test):
                test()
                results["pass"].append(name)
            else:
                results["error"].append(name)
        except AssertionError:
            results["fail"].append(name)
        except Exception:
            results["error"].append(name)
        finally:
            end = time.time()
            length = end - start
            print(f"Ran test {name} - Took {length:.2f} seconds")

        if teardown_func:
            teardown_func()

    for result, val in results.items():
        print(f"{len(val)} {result.title()} Tests")
        for i in val:
            print(f"- {i}")
        print()


if __name__ == "__main__":
    pattern = None
    args = sys.argv[1:]

    if len(args) == 2:
        if args[0] in ("-s", "--select"):
            pattern = args[1]
            print(pattern)

    run_tests(pattern)
