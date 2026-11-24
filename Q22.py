"""Assignment 4 - Question 22
Function to find largest list element.
Run this file directly in VS Code.
"""

def largest(items):
    return max(items)
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print(largest(numbers))
