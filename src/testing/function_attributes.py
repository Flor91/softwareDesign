import pprint


def example():
    """Docstring for example."""
    print("Inside example")


pprint.pprint(dir(example))
print("docstring:", example.__doc__)
print("name:", example.__name__)
