## Object-Oriented Programming

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

- Objects are useful without classes, but classes make them easier to understand.
- A well-designed class defines a **contract** that code using its instances can rely on.
- Objects that respect the same contract are **polymorphic**, i.e., they can be used interchangeably even if they do different specific things.
- Objects and classes can be thought of as dictionaries with stereotyped behavior.
- Most languages allow functions and methods to take a variable number of arguments.
- **Inheritance** can be implemented in several ways that differ in the order in which objects and classes are searched for methods.

Invented to solve two problems:
1. What is the natural way of representing real-world "things" in code?
2. How can we organize our code to make it easier to understand, test and extend?


### Objects

Let's define a Shape:
```python
class Shape:
	def __init__(self, name):
		self.name = name

	def perimeter(self):
		raise NotImplementedError("perimeter")
		
	def area(self):
		raise NotImplementedError("area")
```

A specification like this is a *contract* because an object must satisfy it in order to be considered a shape.

We can **derive** classes from Shape to represent squares and circles.

```python
class Square(Shape):
	def __init__(self, name, side):
		super().__init__(name)
		self.side = side

	def perimeter(self):
		return 4 * self.side
		
	def area(self):
		return self.side ** 2


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2
```

Since squares and circles have the same methods, we can use them interchangeably. This is called **polymorphism**, and it reduces cognitive load by allowing the people using related things to ignore their differences.

> Having many different implementations of the same interface. If a set of functions or objects are polymorphic, they can be called interchangeably

```python
examples = [Square("sq", 3), Circle("ci", 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f"{n} has perimeter {p:.2f} and area {a:.2f}")
```

![](Pasted%20image%2020240626113600.png)


Classes define contracts, by defining methods.
These methods include a constructor.
Objects are instances of a Class.
Objects has attributes.

Python allows for *multiple inheritance* - Inheriting from two or more classes when creating a new class.
*Class methods* are functions defined inside a class, that takes class object as an input instead of an instance of a class.
*Static methods* are functions defined within a class that do not require either the class itself or an instance of a class as a parameter.
*Cache*: Something that stores copies of data so that future requests for it can be satisfied more quickly. The CPU in a computer uses a hardware cache to hold recently-accessed values; many programs rely on a software cache to reduce network traffic and latency.
