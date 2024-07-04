"""
This script identifies duplicate files based on their byte content. It compares 
the contents of files listed in the command line arguments and prints pairs of 
files that have identical contents.

Functions:
- same_bytes(left, right): Compares the byte content of two files.
- find_duplicates(filenames): Finds and returns a list of duplicate files from 
  the provided list of filenames.

Execution:
When run as a script, it takes file paths as command line arguments, finds 
duplicate files among them, and prints the pairs of duplicates.
"""

import sys


def same_bytes(left, right):
    """
    Compare the byte content of two files.

    :param left: Path to the first file.
    :type left: str
    :param right: Path to the second file.
    :type right: str
    :return: True if the byte contents of both files are identical, else False.
    :rtype: bool
    """
    left_bytes = open(left, "rb").read()
    right_bytes = open(right, "rb").read()
    return left_bytes == right_bytes


def find_duplicates(filenames):
    """
    Find and return pairs of duplicate files from a list of filenames.

    :param filenames: List of file paths to check for duplicates.
    :type filenames: list
    :return: List of tuples, each containing a pair of duplicate file paths.
    :rtype: list of tuples
    """
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    """
    Get filenames from command line arguments, find duplicates, and print matches.
    """
    filenames = sys.argv[1:]
    duplicates = find_duplicates(filenames)

    for pair in duplicates:
        print(pair)
