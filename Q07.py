"""Assignment 4 - Question 7
Calculate factorial using math module.
Run this file directly in VS Code.
"""

import math
n = int(input("Enter a non-negative integer: "))
print("Factorial =", math.factorial(n) if n >= 0 else "Invalid input")
