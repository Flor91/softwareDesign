import sys


def same_bytes(left, right):
    left_bytes = open(left, "rb").read()
    right_bytes = open(right, "rb").read()
    return left_bytes == right_bytes


def find_duplicates(filenames):
    """Get list of filenames, find duplicates and returns matches"""
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    filenames = sys.argv[1:]
    duplicates = find_duplicates(filenames)

    for pair in duplicates:
        print(pair)