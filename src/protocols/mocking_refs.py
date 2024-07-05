import time


def elapsed(since):
    return time.time() - since


def mock_time():
    return 200


def test_elapsed():
    # Here we are mocking the time.time function with our own:
    time.time = mock_time
    assert elapsed(50) == 150


class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, arg):
        return arg + self.value


add_3 = Adder(3)
result = add_3(8)
print(f"add_3(8): {result}")  # add_3(8): 11
