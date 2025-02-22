from matching_patterns import Any, Either, Lit


# Test Lit class
def test_literal_match_entire_string():
    assert Lit("abc").match("abc")


def test_literal_substring_alone_no_match():
    assert not Lit("ab").match("abc")


def test_literal_superstring_no_match():
    assert not Lit("abc").match("ab")


def test_literal_followed_by_literal_match():
    # /a/+/b/ matches "ab"
    assert Lit("a", Lit("b")).match("ab")


def test_literal_followed_by_literal_no_match():
    # /a/+/b/ doesn't match "ac"
    assert not Lit("a", Lit("b")).match("ac")


# Test Any class
def test_any_matches_empty():
    # /*/ matches ""
    assert Any().match("")


def test_any_matches_entire_string():
    # /*/ matches "abc"
    assert Any().match("abc")


def test_any_matches_as_prefix():
    # /*def/ matches "abcdef"
    assert Any(Lit("def")).match("abcdef")


def test_any_matches_as_suffix():
    # /abc*/ matches "abcdef"
    assert Lit("abc", Any()).match("abcdef")


def test_any_matches_interior():
    # /a*c/ matches "abc"
    assert Lit("a", Any(Lit("c"))).match("abc")


def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")


def test_either_two_literals_not_both():
    # /{a,b}/ doesn't match "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")


def test_either_followed_by_literal_match():
    # /{a,b}c/ matches "ac"
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")


def test_either_followed_by_literal_no_match():
    # /{a,b}c/ doesn't match "ax"
    assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")
