import sys
from hashlib import sha3_256


def find_groups(filename):
    groups = {}
    for fn in filename:
        data = open(fn, "rb").read()
        hash_code = sha3_256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))
