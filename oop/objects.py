# Section 2.1 - Objects
import math


class Shape:
    """Generic shape class."""
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("Perimeter not implemented")

    def area(self):
        raise NotImplementedError("Area not implemented")

    def density(self, weight):
        return weight / self.area()


class Square(Shape):
    """Square shape class."""
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    """Circle shape class."""
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


examples = [Square("square", 3), Circle("circle", 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    d = thing.density(5)
    print(f"{n} has perimeter {p:.2f} and area {a:.2f} and density {d:.2f}")
