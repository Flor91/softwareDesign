class Parser:
    def __init__(self):
        pass

    def _parse(self, tokens):
        if not tokens:
            return Null()

        front, back = tokens[0], tokens[1:]
        match front[0]:
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
        return Any(self._parse(back))

    def _parse_Lit(self, rest, back):
        return Lit(rest[0], self._parse(back))

    def _parse_EitherStart(self, rest, back):
        children = []
        while back and (back[0][0] == "Lit"):
            children.append(Lit(back[0][1]))
            back = back[1:]

        if not children:
            raise ValueError("empty Either")

        if back[0][0] != "EitherEnd":
            raise ValueError("badly-formatted Either")

        return Either(children, self._parse(back[1:]))

