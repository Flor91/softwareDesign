"""Tokenize a text
Parser's first step. The first stage groups characters into atoms of text called “tokens“,
which are meaningful pieces of text like the digits making up a number or the letters making up a variable name.
Our grammar’s tokens are the special characters ,, {, }, and *.
Any sequence of one or more other characters is a single multi-letter token.

1. If a character is not special, then append it to the current literal (if there is one) or start a new literal (if there isn’t).
2. If a character is special, then close the existing literal (if there is one) and create a token for the special character.

The result of tokenization is a flat list of tokens. The second stage of parsing assembles tokens to create an abstract syntax tree (AST) that represents the structure of what was parsed.
"""
import string

CHARS = set(string.ascii_letters + string.digits)


class Tokenizer:
    def __init__(self):
        self._setup()

    def _setup(self):
        self.result = []
        self.current = ""

    def _add(self, thing):
        if len(self.current) > 0:
            self.result.append(["Lit", self.current])
            self.current = ""
        if thing is not None:
            self.result.append([thing])

    def tok(self, text):
        self._setup()
        for ch in text:
            if ch == "*":
                self._add("Any")
            elif ch == "{":
                self._add("EitherStart")
            elif ch == ",":
                self._add(None)
            elif ch == "}":
                self._add("EitherEnd")
            elif ch in CHARS:
                self.current += ch
            else:
                raise NotImplementedError(f"What is '{ch}'?")
        self._add(None)
        return self.result


