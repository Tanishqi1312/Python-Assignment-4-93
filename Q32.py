"""Assignment 4 - Question 32
Demonstrate variable-length *args.
Run this file directly in VS Code.
"""

def add_all(*args):
    return sum(args)
print(add_all(10, 20, 30, 40))
