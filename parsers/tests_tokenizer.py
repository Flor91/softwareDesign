from tokenizer import Tokenizer
from parser import Parser
from Globs.matching_patterns import Lit, Either


def test_tok_empty_string():
    assert Tokenizer().tok("") == []


def test_tok_any_either():
    assert Tokenizer().tok("*{abc,def}a") == [
        ["Any"],
        ["EitherStart"],
        ["Lit", "abc"],
        ["Lit", "def"],
        ["EitherEnd"],
        ["Lit", "a"]
    ]


def test_parse_either_two_lit():
    assert Parser()._parse("{abc,def}") == Either(
        [Lit("abc"), Lit("def")]
    )