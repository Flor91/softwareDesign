# Functions and Closures

When we define a function, our programming system saves instructions for later use.
Since functions are just data, we can separate creation from naming.
Most programming languages use eager evaluation, in which arguments are evaluated before a function is called.
Programming languages can also use lazy evaluation, in which expressions are passed to functions for just-in-time evaluation.
Every call to a function creates a new stack frame on the call stack.
When a function looks up variables it checks its own stack frame and the global frame.
A closure stores the variables referenced in a particular scope.

One way to evaluate the design of a piece of software is to ask how extensible it is, i.e., how easily we can add or change things.


### Glossary
anonymous function
A function without a name. Languages like JavaScript make frequent use of anonymous functions; Python provides a limited form called a lambda expression.

call stack
A data structure that stores information about the active subroutines executed.

closure
A record that stores a function and its environment so that variables that were in scope when the function was defined can still be accessed from within the function even if they are no longer visible to other parts of the program.

dynamic scoping
To find the value of a variable by looking at what is on the call stack at the moment the lookup is done. Almost all programming languages use lexical scoping instead, since it is more predictable

eager evaluation
Evaluating expressions before they are used.

extensibility
How easily new features can be added to a program or existing features can be changed.

lambda expression
An expression that takes zero or more parameters and produces a result. A lambda expression is sometimes called an anonymous function; the name comes from the mathematical symbol λ used to represent such expressions.

lazy evaluation
Evaluating expressions only when absolutely necessary.

lexical scoping
To look up the value associated with a name according to the textual structure of a program. Most programming languages use lexical scoping instead of dynamic scoping because the latter is less predictable.

name collision
A situation in which two or more things are trying to use the same name at the same time or in the same scope.

stack frame
A section of the call stack that records details of a single call to a specific function.

variable capture
The process by which a closure “remembers” the variables that were in scope when it was created.
