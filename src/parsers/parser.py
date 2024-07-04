"""
This module provides a Parser class for parsing token sequences into specific pattern objects.
The patterns include Null, Any, Lit, and Either, each represented by corresponding classes.
"""

from src.globs.matching_patterns import Any, Either, Lit, Null


class Parser:
    def __init__(self):
        pass

    def _parse(self, tokens):
        """
        Parses a list of tokens into corresponding pattern objects.

        :param tokens: List of tokens to be parsed
        :type tokens: list
        :raises AssertionError: If an unknown token type is encountered
        :return: Parsed pattern object
        :rtype: object
        """
        if not tokens:
            return Null()

        front, back = tokens[0], tokens[1:]
        first = front[0]
        match first:
            case "Any":
                handler = self._parse_Any
            case "EitherStart":
                handler = self._parse_EitherStart
            case "Lit":
                handler = self._parse_Lit
            case _:
                assert False, f"Unknown token type {front}"

        return handler(front[1:], back)

    def _parse_Any(self, rest, back):
        """
        Parses 'Any' tokens into Any pattern object.

        :param rest: Remaining tokens after 'Any'
        :type rest: list
        :param back: Back tokens
        :type back: list
        :return: Any pattern object
        :rtype: Any
        """
        return Any(self._parse(back))

    def _parse_Lit(self, rest, back):
        """
        Parses 'Lit' tokens into Lit pattern object.

        :param rest: Remaining tokens after 'Lit'
        :type rest: list
        :param back: Back tokens
        :type back: list
        :return: Lit pattern object
        :rtype: Lit
        """
        return Lit(rest[0], self._parse(back))

    def _parse_EitherStart(self, rest, back):
        """
        Parses 'EitherStart' tokens into Either pattern object.

        :param rest: Remaining tokens after 'EitherStart'
        :type rest: list
        :param back: Back tokens
        :type back: list
        :raises ValueError: If 'Either' is empty or badly formatted
        :return: Either pattern object
        :rtype: Either
        """
        children = []
        while back and (back[0][0] == "Lit"):
            children.append(Lit(back[0][1]))
            back = back[1:]

        if not children:
            raise ValueError("empty Either")

        if back[0][0] != "EitherEnd":
            raise ValueError("badly-formatted Either")

        return Either(children, self._parse(back[1:]))
