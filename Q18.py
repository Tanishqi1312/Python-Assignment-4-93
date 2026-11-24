"""Assignment 4 - Question 18
Function to check prime.
Run this file directly in VS Code.
"""

def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n ** 0.5) + 1))
print("Prime" if is_prime(int(input("Number: "))) else "Not prime")
