import sys
from hashlib import sha3_256


def find_groups(filename):
    """Find groups of filenames based on their SHA3-256 hash.

    :param filename: List of filenames to group.
    :type filename: list
    :return: Dictionary where keys are SHA3-256 hashes are sets of filenames.
    :rtype: dict
    """
    groups = {}
    for fn in filename:
        data = open(fn, "rb").read()
        hash_code = sha3_256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    """Get filenames from command line arguments,
    group them by SHA3-256 hash, and print each group.
    """
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))
