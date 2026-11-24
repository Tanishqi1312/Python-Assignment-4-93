"""Assignment 4 - Question 9
Calculate sine, cosine and tangent for an angle.
Run this file directly in VS Code.
"""

import math
degrees = float(input("Enter angle in degrees: "))
radians = math.radians(degrees)
print("Sine:", math.sin(radians))
print("Cosine:", math.cos(radians))
print("Tangent:", math.tan(radians))
