"""Assignment 4 - Question 21
Function to calculate digit sum.
Run this file directly in VS Code.
"""

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))
print(digit_sum(int(input("Enter integer: "))))
