[Software Design by Example](https://third-bit.com/sdxpy/)

> The complexity of a system increases more rapidly than its size.

As the number of components in a system grows, so does the complexity. However, the number of things that can be held in working memory is fixed and small. So, if we want to build large understandable programs, we need to do them modular - out of small pieces that can interact with each other. Figuring our **what those pieces are and their interactions** is the core of "designing" a system.

## Designing a System

1. [Objects and Classes](oop/OOP.md)
   1. [Basic Objects definitions](oop/objects.py)
   2. [Arguments](oop/arguments.py)
   3. [Implementation of Objects as dictionary of functions](oop/dictionary_functions.py)
2. [Hashing](hashing/hashing.md)
   1. [Finding duplicate files - Brute force approach](hashing/force_brute.py)
   2. [Finding duplicate files - Hashing approach](hashing/sha256_hashing.py)
3. [Globs](globs/matching_patterns.md)
   1. [Implement Matching patterns](globs/matching_patterns.py) 
4. [Parsers](parsers/parsing.md)
   1. [Implement a Tokenizer](parsers/tokenizer.py)
   2. [Implement a Parser](parsers/parser.py)
5. [Testing](testing/running_tests.md)
   1. [Introspection](testing/instrospection.py)
   2. [Running tests](testing/testing.py)
6. [Interpreters](interpreters/interpreters.md)
   1. 