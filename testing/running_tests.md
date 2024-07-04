# Running Tests

### Summary of Main Takeaways
- Understand the nature of functions in Python.
- Learn how Python manages local and global variables.
- Grasp the concept of unit tests and their outcomes.
- Comprehend the role of introspection in finding functions and objects at runtime.

### Detailed Notes

#### Functions as Objects
- **Functions are objects**: In Python, functions are first-class objects, which means you can:
  - Save them in data structures (e.g., lists, dictionaries).
  - Pass them as arguments to other functions.
  - Return them from other functions.

#### Variable Storage
- **Local and Global Variables**: Python stores variables in dictionary-like structures:
  - **Local variables**: Stored in the local namespace.
  - **Global variables**: Stored in the global namespace.
  - These namespaces are essentially dictionaries where variable names are keys and their values are the corresponding objects.

#### Unit Testing
- **Unit Test**: A unit test is a test that:
  - **Performs an operation** on a piece of code called a fixture.
  - **Outcomes**: The test can either pass, fail, or produce an error.
  - **Purpose**: Ensure that the fixture behaves as expected under various conditions.

#### Introspection
- **Introspection**: The ability of a program to examine the type or properties of an object at runtime.
  - **Uses**: A program can use introspection to:
    - Find functions.
    - Discover other objects.
  - This helps in dynamically interacting with objects, especially useful in testing and debugging.

### Examples and Illustrations

#### Example of Functions as Objects
```python
def greet(name):
    return f"Hello, {name}!"

# Saving function in a list
functions_list = [greet]

# Passing function as an argument
def call_function(func, name):
    return func(name)

print(call_function(greet, "Alice"))  # Output: Hello, Alice!
```

#### Example of Unit Test
```python
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

#### Example of Introspection
```python
def sample_function():
    pass

# Using introspection to find the name of the function
print(sample_function.__name__)  # Output: sample_function

# Finding all attributes of the function
print(dir(sample_function))
```

### Tables and Diagrams

#### Table: Variable Storage
| Type of Variable | Namespace         | Example                       |
|------------------|-------------------|-------------------------------|
| Local            | Local Namespace   | Variables inside a function   |
| Global           | Global Namespace  | Variables outside any function|
