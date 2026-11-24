"""Assignment 4 - Question 23
Function to calculate average of list.
Run this file directly in VS Code.
"""

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
values = list(map(float, input("Enter numbers: ").split()))
print("Average =", average(values))
