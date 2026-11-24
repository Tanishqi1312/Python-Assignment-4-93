"""Assignment 4 - Question 8
Calculate GCD and LCM.
Run this file directly in VS Code.
"""

import math
a, b = map(int, input("Enter two integers: ").split())
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd if gcd else 0
print("GCD:", gcd, "LCM:", lcm)
