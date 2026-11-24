"""Assignment 4 - Question 16
Function to find greatest of three numbers.
Run this file directly in VS Code.
"""

def greatest(a, b, c):
    return max(a, b, c)
print(greatest(*map(float, input("Enter three numbers: ").split())))
