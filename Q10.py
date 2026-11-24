"""Assignment 4 - Question 10
Demonstrate ceil(), floor() and sqrt().
Run this file directly in VS Code.
"""

import math
n = float(input("Enter number: "))
print("Ceil:", math.ceil(n))
print("Floor:", math.floor(n))
print("Square root:", math.sqrt(n) if n >= 0 else "Not real")
