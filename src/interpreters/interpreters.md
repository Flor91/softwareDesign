# Interpreters

- **Compilers and interpreters are just programs**: They both serve the purpose of converting high-level code into executable instructions.
- **Basic arithmetic operations are just functions that have special notation**: Operations like addition and multiplication are functions with symbols like `+` and `*`.
- **Programs can be represented as trees, which can be stored as nested lists**: This representation helps in understanding the structure and flow of the program.
- **Interpreters recursively dispatch operations to functions that implement low-level steps**: This means that interpreters break down operations into smaller steps and call specific functions to handle them.
- **Programs store variables in stacked dictionaries called environments**: This allows for organized and manageable storage of variables.
- **One way to evaluate a program's design is to ask how extensible it is**: A well-designed program should be easy to extend and modify.

## Detailed Notes

### Compilers and Interpreters
- **Definition**: Both are types of programs that convert high-level code into a form that can be executed by a computer.
- **Compilers**: Translate the entire program into machine code before execution.
- **Interpreters**: Translate and execute code line-by-line.

### Arithmetic Operations
- **Special Notation**: Basic operations like addition, subtraction, multiplication, and division are functions with unique symbols.
- **Example**:
  - Addition (`+`): `3 + 2`
  - Subtraction (`-`): `5 - 1`
  - Multiplication (`*`): `4 * 2`
  - Division (`/`): `8 / 4`

### Program Representation
- **Tree Structure**: Programs can be represented as trees, which help in visualizing the hierarchical structure of code.
- **Nested Lists**: These trees can be stored as nested lists in programming languages.
- **Example**:
  ```python
  tree = ['+', ['*', 2, 3], 4]  # Represents (2 * 3) + 4
  ```

### Interpreter Operations
- **Recursive Dispatch**: Interpreters use recursion to handle operations, calling specific functions for each low-level task.
- **Function Implementation**: Each operation is implemented as a function that handles the specific steps required.

### Variable Storage
- **Environments**: Variables are stored in environments, which are essentially stacked dictionaries.
- **Stacked Dictionaries**: This structure allows for variable scope and lifetime management.
- **Example**:
  ```python
  env = {'x': 10, 'y': 20}
  ```

### Program Design Evaluation
- **Extensibility**: A key factor in evaluating a program's design is how easily it can be extended or modified.
- **Questions to Ask**:
  - Can new features be added without major changes to existing code?
  - How modular is the program?
