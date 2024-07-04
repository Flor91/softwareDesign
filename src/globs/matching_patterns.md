# Matching Patterns

## Key Concepts

- **Globbing** and **regular expressions** are essential for pattern matching in text.
- **Inheritance** and **delegation** help in creating modular and maintainable code.
- The **Null Object Pattern** and **Chain of Responsibility Pattern** are useful design patterns for handling special cases and creating processing chains, respectively.
- **Refactoring** techniques and **prototyping** are crucial for improving and validating code design.

## Detailed Notes

### Globbing
- **Definition**: Matching filenames against patterns.
- **Origin**: From Unix utility `glob` (short for “global”).
- **Usage**: Useful for matching sets of filenames using wildcards like `*` and `?`.

### Regular Expressions
- **Definition**: A pattern for matching text, written as text itself.
- **Applications**: Used for searching, replacing, and parsing text.

### Chain of Responsibility Pattern
- **Definition**: A design pattern where each object either handles a request or passes it on to another object.
- **Usage**: Helps in creating a chain of processing objects.

### Extract Parent Class Refactoring
- **Definition**: Moving common functionality from existing classes to a new parent class.
- **Benefit**: Encourages code reuse and cleaner class hierarchies.

### Null Object Pattern
- **Definition**: A design pattern where a placeholder object is used instead of `None`.
- **Benefit**: Avoids repetitive `None` checks and simplifies code logic.

### Inheritance for Composable and Extensible Matchers
- **Concept**: Using inheritance to create flexible matchers that can be easily extended.
- **Benefit**: Makes the codebase more modular and easier to maintain.

### Delegation for Simplifying Code
- **Concept**: Objects delegate tasks to other objects.
- **Benefit**: Reduces complexity and promotes single responsibility principle.

### Refactoring Techniques
- **Concept**: Moving code from one working state to another.
- **Benefit**: Improves code quality and maintainability without changing its functionality.

### Prototyping to Validate Design
- **Concept**: Build and check the parts of your code you are least sure of first.
- **Benefit**: Helps in quickly finding out if your design will work.
