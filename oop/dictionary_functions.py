# Sore function objects in data structures - dicts and lists
import math


def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }


def shape_density(thing, weight):
    return weight / call(thing, "area")


Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": None,
    "_new": shape_new
}


# SQUARE FUNCTIONS
def square_perimeter(thing):
    """Square perimeter method."""
    return 4 * thing["side"]


def square_area(thing):
    """Square area method."""
    return thing["side"] ** 2


def square_larger(thing, size):
    """Whether the square is larger than a provided size."""
    return call(thing, "area") > size


def square_new(name, side):
    """Define a new Square."""
    return make(Shape, name) | {
        "side": side,
        "_class": Square
    }


Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_classname": "Square",
    "_parent": [Shape],
    "_new": square_new
}


# CIRCLE FUNCTIONS
def circle_perimeter(thing):
    """Circle perimeter method."""
    return 2 * math.pi * thing["radius"]


def circle_area(thing):
    """Circle area method."""
    return math.pi * thing["radius"] ** 2


def circle_larger(thing, size):
    """Whether the circle is larger than a provided size."""
    return call(thing, "area") > size


def circle_new(name, radius):
    """Define a new Circle."""
    return make(Shape, name) | {
        "radius": radius,
        "_class": Circle
    }


Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "larger": circle_larger,
    "_classname": "Circle",
    "_parent": [Shape],
    "_new": circle_new
}


def make(cls, *args):
    return cls["_new"](*args)


def find(cls, method_name):
    for c in [cls] + cls["_parent"]:
        if c is not None and method_name in c:
            return c[method_name]
    raise NotImplementedError("method_name")


def call(thing, method_name, *args, **kwargs):
    """Generic Function to call classes methods."""
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)


# Example to try the polymorphism of objects and classes
examples = [make(Square, "sq", 3), make(Circle,"ci", 2)]
l = 10
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex, "area")
    c = ex["_class"]["_classname"]
    d = call(ex, "density", **{"weight": 5})
    print(f"{n} is a {c} and has perimeter {p:.2f} and area {a:.2f} and density of {d:.2f}")

    r = call(ex, "larger", **{"size": l})
    print(f"Is {n} larger than {l}? {r}")

