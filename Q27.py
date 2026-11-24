"""Assignment 4 - Question 27
Function accepting three numbers and returning greatest.
Run this file directly in VS Code.
"""

def greatest(a, b, c):
    return max(a, b, c)
print(greatest(*map(float, input("Enter three numbers: ").split())))
