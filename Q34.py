"""Assignment 4 - Question 34
Function returning uppercase and lowercase counts.
Run this file directly in VS Code.
"""

def count_case(text):
    upper = sum(ch.isupper() for ch in text)
    lower = sum(ch.islower() for ch in text)
    return upper, lower
print(count_case(input("Enter text: ")))
