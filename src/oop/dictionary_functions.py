import math


def shape_new(name):
    """
    Create a new shape.

    :param name: The name of the shape.
    :type name: str
    :return: A dictionary representing the shape.
    :rtype: dict
    """
    return {
        "name": name,
        "_class": Shape
    }


def shape_density(thing, weight):
    """
    Calculate the density of a shape.

    :param thing: The shape object.
    :type thing: dict
    :param weight: The weight of the shape.
    :type weight: float
    :return: The density of the shape.
    :rtype: float
    """
    return weight / call(thing, "area")


Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": None,
    "_new": shape_new
}


# SQUARE FUNCTIONS
def square_perimeter(thing):
    """
    Calculate the perimeter of a square.

    :param thing: The square object.
    :type thing: dict
    :return: The perimeter of the square.
    :rtype: float
    """
    return 4 * thing["side"]


def square_area(thing):
    """
    Calculate the area of a square.

    :param thing: The square object.
    :type thing: dict
    :return: The area of the square.
    :rtype: float
    """
    return thing["side"] ** 2


def square_larger(thing, size):
    """
    Check if the square is larger than a provided size.

    :param thing: The square object.
    :type thing: dict
    :param size: The size to compare with.
    :type size: float
    :return: True if the square is larger than the provided size, else False.
    :rtype: bool
    """
    return call(thing, "area") > size


def square_new(name, side):
    """
    Create a new square.

    :param name: The name of the square.
    :type name: str
    :param side: The side length of the square.
    :type side: float
    :return: A dictionary representing the square.
    :rtype: dict
    """
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
    """
    Calculate the perimeter of a circle.

    :param thing: The circle object.
    :type thing: dict
    :return: The perimeter of the circle.
    :rtype: float
    """
    return 2 * math.pi * thing["radius"]


def circle_area(thing):
    """
    Calculate the area of a circle.

    :param thing: The circle object.
    :type thing: dict
    :return: The area of the circle.
    :rtype: float
    """
    return math.pi * thing["radius"] ** 2


def circle_larger(thing, size):
    """
    Check if the circle is larger than a provided size.

    :param thing: The circle object.
    :type thing: dict
    :param size: The size to compare with.
    :type size: float
    :return: True if the circle is larger than the provided size, else False.
    :rtype: bool
    """
    return call(thing, "area") > size


def circle_new(name, radius):
    """
    Create a new circle.

    :param name: The name of the circle.
    :type name: str
    :param radius: The radius of the circle.
    :type radius: float
    :return: A dictionary representing the circle.
    :rtype: dict
    """
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
    """
    Create a new instance of a class.

    :param cls: The class to instantiate.
    :type cls: dict
    :return: A new instance of the class.
    :rtype: dict
    """
    return cls["_new"](*args)


def find(cls, method_name):
    """
    Find a method in the class or its parent classes.

    :param cls: The class to search in.
    :type cls: dict
    :param method_name: The name of the method to find.
    :type method_name: str
    :raises NotImplementedError: If the method is not found.
    :return: The method if found.
    :rtype: function
    """
    for c in [cls] + cls["_parent"]:
        if c is not None and method_name in c:
            return c[method_name]
    raise NotImplementedError("method_name")


def call(thing, method_name, *args, **kwargs):
    """
    Call a method of a class.

    :param thing: The object to call the method on.
    :type thing: dict
    :param method_name: The name of the method to call.
    :type method_name: str
    :param *args: Arguments to pass to the method.
    :type *args: tuple
    :param **kwargs: Keyword arguments to pass to the method.
    :type **kwargs: dict
    :return: The result of the method call.
    :rtype: any
    """
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
