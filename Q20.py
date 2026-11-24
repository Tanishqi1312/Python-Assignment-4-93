"""Assignment 4 - Question 20
Function to reverse string.
Run this file directly in VS Code.
"""

def reverse_string(text):
    result = ""
    for ch in text: result = ch + result
    return result
print(reverse_string(input("Enter text: ")))
