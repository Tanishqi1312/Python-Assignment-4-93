"""Assignment 4 - Question 6
Calculate square root using math module.
Run this file directly in VS Code.
"""

import math
n = float(input("Enter number: "))
if n < 0: print("Square root of a negative number is not real.")
else: print("Square root =", math.sqrt(n))
