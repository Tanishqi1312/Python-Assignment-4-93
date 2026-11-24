"""Assignment 4 - Question 17
Function to calculate factorial.
Run this file directly in VS Code.
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1): result *= i
    return result
n = int(input("Non-negative integer: "))
print(factorial(n) if n >= 0 else "Invalid input")
