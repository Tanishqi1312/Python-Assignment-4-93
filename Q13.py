"""Assignment 4 - Question 13
Function to calculate circle area.
Run this file directly in VS Code.
"""

def circle_area(radius):
    return 3.141592653589793 * radius ** 2
r = float(input("Radius: "))
print("Area =", circle_area(r))
