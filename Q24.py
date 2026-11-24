"""Assignment 4 - Question 24
Function to count vowels.
Run this file directly in VS Code.
"""

def count_vowels(text):
    return sum(ch.lower() in "aeiou" for ch in text)
print(count_vowels(input("Enter text: ")))
