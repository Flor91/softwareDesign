def show_args(title, *args, **kwargs):
    """
    Show how arguments work.

    :param title: The title or main descriptor.
    :type title: str
    :param *args: Variable length argument list.
    :type *args: tuple
    :param **kwargs: Arbitrary keyword arguments.
    :type **kwargs: dict
    """
    print(f"{title} has arguments: '{args}' and kwargs: '{kwargs}'")


# Demonstrate the usage of variable arguments and keyword arguments
show_args("nothing")  # nothing has arguments: '()' and kwargs: '{}'
show_args("one unnamed arg", 1)  # one unnamed arg has arguments: '(1,)' and kwargs: '{}'
show_args("one named arg", second="2")  # one named arg has arguments: '()' and kwargs: '{'second': '2'}'
show_args("one of each", 3, fourth="4")  # one of each has arguments: '(3,)' and kwargs: '{'fourth': '4'}'


def show_spread(left, middle, right):
    """
    Show how spreading arguments from a list or dict works.

    :param left: The left argument.
    :type left: any
    :param middle: The middle argument.
    :type middle: any
    :param right: The right argument.
    :type right: any
    """
    print(f"Left: {left} - Middle: {middle} - Right: {right}")


# Demonstrate spreading arguments from a list
all_in_list = [1, 2, 3]
show_spread(*all_in_list)  # Left: 1 - Middle: 2 - Right: 3

# Demonstrate spreading arguments from a dictionary
all_in_dict = {"right": 30, "left": 10, "middle": 20}
show_spread(**all_in_dict)  # Left: 10 - Middle: 20 - Right: 30
