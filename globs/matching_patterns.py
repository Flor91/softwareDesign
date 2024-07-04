class Match:
    def __init__(self, rest):
        self.rest: Match = rest if rest is not None else Null()

    def match(self, text):
        result = self._match(text, 0)
        return result == len(text)


class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        return start


class Lit(Match):
    """Matcher that checks whether a piece of fixed text matches a string.

    Used for matching literals. A representation of a fixed value in a program,
    such as the digits 123 for the number 123 or the characters "abc"
    for the string containing those three letters.
    """
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text, start=0):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)


class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start=0):
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None


class Either(Match):
    def __init__(self, left, right, rest=None):
        super().__init__(rest)
        self.left = left
        self.right = right

    def _match(self, text, start=0):
        for pat in [self.left, self.right]:
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None

