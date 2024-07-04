"""Basic Objects definitions in Python."""

import math


class Shape:
    """Generic shape abstract class.

    This class needs to be inherited,
    and methods need to be defined by its child classes.
    This is a blueprint of how Shapes need to be defined.

    Attributes
    ----------
    name : str
        The name of the shape.

    Methods
    -------
    perimeter(): Abstract method to calculate the perimeter of the shape.
    area(): Abstract method to calculate the area of the shape.
    density(weight: float) -> float: Calculates the density of the shape.
    """

    def __init__(self, name):
        """
        Parameters
        ----------
        name : str
            The name of the shape.
        """
        self.name = name

    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in the child class.
        """
        raise NotImplementedError("Perimeter not implemented")

    def area(self):
        """Abstract method to calculate the area of the shape.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in the child class.
        """
        raise NotImplementedError("Area not implemented")

    def density(self, weight):
        """Calculates the density of the shape given its weight.

        Parameters
        ----------
        weight : float
            The weight of the shape.

        Returns
        -------
        float
            The density of the shape.
        """
        return weight / self.area()


class Square(Shape):
    """Square shape class.

    Attributes
    ----------
    name : str
        The name of the shape.
    side : float
        The length of one side of the square.

    Methods
    -------
    perimeter() -> float:
        Calculates the perimeter of the square.
    area() -> float:
        Calculates the area of the square.
    """

    def __init__(self, name, side):
        """
        Parameters
        ----------
        name : str
            The name of the square.
        side : float
            The length of one side of the square.
        """
        super().__init__(name)
        self.side = side

    def perimeter(self):
        """Calculates the perimeter of the square.

        Returns
        -------
        float
            The perimeter of the square.
        """
        return 4 * self.side

    def area(self):
        """Calculates the area of the square.

        Returns
        -------
        float
            The area of the square.
        """
        return self.side**2


class Circle(Shape):
    """Circle shape class.

    Attributes
    ----------
    name : str
        The name of the shape.
    radius : float
        The radius of the circle.

    Methods
    -------
    perimeter() -> float:
        Calculates the perimeter of the circle.
    area() -> float:
        Calculates the area of the circle.
    """

    def __init__(self, name, radius):
        """
        Parameters
        ----------
        name : str
            The name of the circle.
        radius : float
            The radius of the circle.
        """
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        """Calculates the perimeter of the circle.

        Returns
        -------
        float
            The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self):
        """Calculates the area of the circle.

        Returns
        -------
        float
            The area of the circle.
        """
        return math.pi * self.radius**2


"""Objects with the same methods allow us to use polymorphism."""
examples = [Square("square", 3), Circle("circle", 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    d = thing.density(5)
    print(f"{n} has perimeter {p:.2f} and area {a:.2f} and density {d:.2f}")
