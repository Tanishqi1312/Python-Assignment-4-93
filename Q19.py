"""Assignment 4 - Question 19
Function to check palindrome string.
Run this file directly in VS Code.
"""

def is_palindrome(text):
    cleaned = text.replace(" ", "").casefold()
    return cleaned == cleaned[::-1]
print(is_palindrome(input("Enter text: ")))
