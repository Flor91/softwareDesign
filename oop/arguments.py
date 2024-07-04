# Variable Arguments
def show_args(title, *args, **kwargs):
    """Show how arguments work"""
    print(f"{title} has arguments: '{args}' and kwargs: '{kwargs}'")


show_args("nothing")  # nothing has arguments: '()' and kwargs: '{}'
show_args("one unnamed arg", 1)  # one unnamed arg has arguments: '(1,)' and kwargs: '{}'
show_args("one named arg", second="2")  # one named arg has arguments: '()' and kwargs: '{'second': '2'}'
show_args("one of each", 3, fourth="4")  # one of each has arguments: '(3,)' and kwargs: '{'fourth': '4'}'


def show_spread(left, middle, right):
    print(f"Left: {left} - Middle: {middle} - Right: {right}")


all_in_list = [1, 2, 3]
show_spread(*all_in_list)  # Left: 1 - Middle: 2 - Right: 3

all_in_dict = {"right": 30, "left": 10, "middle": 20}
show_spread(**all_in_dict)  # Left: 10 - Middle: 20 - Right: 30
