"""Assignment 4 - Question 14
Function to find square and cube.
Run this file directly in VS Code.
"""

def square_cube(n):
    return n ** 2, n ** 3
number = float(input("Number: "))
print("Square and cube:", square_cube(number))
