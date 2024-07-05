"""Decorators allows to wrap one functions with another."""


def original(value):
    print(f"Original: {value}")


def logging(func, label):
    def _inner(value):
        print(f"++ {label}")
        func(value)
        print(f"-- {label}")

    return _inner


original = logging(original, "call")
original("example 1")


def wrap(label):
    def _decorate(func):
        def _inner(*args):
            print(f"++ {label}")
            func(*args)
            print(f"-- {label}")

        return _inner

    return _decorate


@wrap("wrapping")
def original2(message):
    print(f"Original: {message}")


original2("example 2")
