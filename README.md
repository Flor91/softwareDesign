# Software Design by Example

> The complexity of a system increases more rapidly than its size.

As the number of components in a system grows, so does the complexity. However, the number of things that can be held in working memory is fixed and small. So, if we want to build large understandable programs, we need to do them modular - out of small pieces that can interact with each other. Figuring our **what those pieces are and their interactions** is the core of "designing" a system.

## Designing a System

1. [Objects and Classes](src/oop/OOP.md)
   1. [Basic Objects definitions](src/oop/objects.py)
   2. [Arguments](src/oop/arguments.py)
   3. [Implementation of Objects as dictionary of functions](src/oop/dictionary_functions.py)
2. [Hashing](src/hashing/hashing.md)
   1. [Finding duplicate files - Brute force approach](src/hashing/force_brute.py)
   2. [Finding duplicate files - Hashing approach](src/hashing/sha256_hashing.py)
3. [Globs](src/globs/matching_patterns.md)
   1. [Implement Matching patterns](src/globs/matching_patterns.py) 
4. [Parsers](src/parsers/parsing.md)
   1. [Implement a Tokenizer](src/parsers/tokenizer.py)
   2. [Implement a Parser](src/parsers/parser.py)
5. [Testing](src/testing/running_tests.md)
   1. [Introspection](src/testing/instrospection.py)
   2. [Running tests](src/testing/testing.py)
6. [Interpreters](src/interpreters/interpreters.md)
   1. 