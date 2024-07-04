"""
Tokenizer for parsing text into meaningful tokens.

This module provides a Tokenizer class to break down text into tokens such as
literals and special characters. It follows a simple grammar where special
characters include '*', '{', '}', and ','. Any sequence of other characters
is considered a literal token.

Classes:
    Tokenizer: A class to tokenize input text based on predefined rules.
"""

import string

CHARS = set(string.ascii_letters + string.digits)


class Tokenizer:
    def __init__(self):
        """Initialize the Tokenizer instance."""
        self._setup()

    def _setup(self):
        """Setup/reset the tokenizer's internal state."""
        self.result = []
        self.current = ""

    def _add(self, thing):
        """Add a token to the result list.

        :param thing: The token to be added.
        :type thing: str or None
        """
        if len(self.current) > 0:
            self.result.append(["Lit", self.current])
            self.current = ""
        if thing is not None:
            self.result.append([thing])

    def tok(self, text):
        """Tokenize the input text.

        :param text: The text to be tokenized.
        :type text: str
        :raises NotImplementedError: If an unknown character is encountered.
        :return: A list of tokens.
        :rtype: list
        """
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
