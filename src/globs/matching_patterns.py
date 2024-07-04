"""
This module provides a set of classes for pattern matching in strings.
It includes classes for matching fixed literals, any characters,
and either of two patterns.
"""


class Match:
    """
    Base class for pattern matching.

    :param rest: The next pattern to match, defaults to None
    :type rest: Match, optional
    """

    def __init__(self, rest=None):
        self.rest: Match = rest if rest is not None else Null()

    def match(self, text):
        """
        Check if the entire text matches the pattern.

        :param text: The text to match against
        :type text: str
        :return: True if the text matches the pattern, False otherwise
        :rtype: bool
        """
        result = self._match(text, 0)
        return result == len(text)

    def __eq__(self, other):
        """
        Check if this pattern is equal to another pattern.

        :param other: The other pattern to compare against
        :type other: Match
        :return: True if the patterns are equal, False otherwise
        :rtype: bool
        """
        return other is not None and self.__class__ == other.__class__ and self.rest == other.rest


class Null(Match):
    """
    Class for matching the end of a string.
    """

    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        """
        Always matches the end of the string.

        :param text: The text to match against
        :type text: str
        :param start: The starting position in the text
        :type start: int
        :return: The starting position
        :rtype: int
        """
        return start


class Lit(Match):
    """
    Matcher that checks whether a piece of fixed text matches a string.

    Used for matching literals. A representation of a fixed value in a program,
    such as the digits 123 for the number 123 or the characters "abc"
    for the string containing those three letters.

    :param chars: The literal text to match
    :type chars: str
    :param rest: The next pattern to match, defaults to None
    :type rest: Match, optional
    """

    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text, start=0):
        """
        Match the literal text starting from the given position.

        :param text: The text to match against
        :type text: str
        :param start: The starting position in the text, defaults to 0
        :type start: int, optional
        :return: The position after the matched text, or None if no match
        :rtype: int or None
        """
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)

    def __eq__(self, other):
        """
        Check if this pattern is equal to another pattern.

        :param other: The other pattern to compare against
        :type other: Match
        :return: True if the patterns are equal, False otherwise
        :rtype: bool
        """
        return super().__eq__(other) and self.chars == other.chars


class Any(Match):
    """
    Matcher that checks whether any character matches.

    :param rest: The next pattern to match, defaults to None
    :type rest: Match, optional
    """

    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start=0):
        """
        Match any character starting from the given position.

        :param text: The text to match against
        :type text: str
        :param start: The starting position in the text, defaults to 0
        :type start: int, optional
        :return: The position after the matched text, or None if no match
        :rtype: int or None
        """
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None


class Either(Match):
    """
    Matcher that checks whether either of two patterns matches.

    :param left: The first pattern to match
    :type left: Match
    :param right: The second pattern to match
    :type right: Match
    :param rest: The next pattern to match, defaults to None
    :type rest: Match, optional
    """

    def __init__(self, left, right, rest=None):
        super().__init__(rest)
        self.left = left
        self.right = right

    def _match(self, text, start=0):
        """
        Match either of the two patterns starting from the given position.

        :param text: The text to match against
        :type text: str
        :param start: The starting position in the text, defaults to 0
        :type start: int, optional
        :return: The position after the matched text, or None if no match
        :rtype: int or None
        """
        for pat in [self.left, self.right]:
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
