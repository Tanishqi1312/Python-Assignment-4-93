"""Assignment 4 - Question 48
Use math module to evaluate a mathematical expression.
Run this file directly in VS Code.
"""

import math
x = float(input("Enter x: "))
print("sqrt(x) + x^2 =", math.sqrt(x) + x ** 2 if x >= 0 else "x must be non-negative")
