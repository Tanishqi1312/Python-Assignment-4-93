"""Assignment 4 - Question 25
Function to find string length without len().
Run this file directly in VS Code.
"""

def string_length(text):
    count = 0
    for _ in text: count += 1
    return count
print(string_length(input("Enter text: ")))
