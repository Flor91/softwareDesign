"""
This script demonstrates basic usage of Python's global and local namespaces.
It includes functions to find and print functions with a specific prefix and to show local variables within a range.
"""

import pprint

var = 123


def find_tests(prefix):
    """
    Finds and prints functions in the global namespace that start with a given prefix.

    :param prefix: The prefix to search for
    :type prefix: str
    """
    for name, func in globals().items():
        if name.startswith(prefix):
            print(name, func)


pprint.pprint(globals())
find_tests("test_")

name = None
for name in globals():
    print(name)


def show_locals(low, high):
    """
    Prints local variables at the start, during, and end of a loop from low to high.

    :param low: The starting value of the range
    :type low: int
    :param high: The ending value of the range
    :type high: int
    """
    print(f"start: {locals()}")
    for i in range(low, high):
        print(f"loop {i}: {locals()}")
    print(f"end: {locals()}")


show_locals(1, 3)
