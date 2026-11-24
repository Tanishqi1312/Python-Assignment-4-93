"""Assignment 4 - Question 28
Function for simple interest using arguments and return.
Run this file directly in VS Code.
"""

def simple_interest(principal, rate, time):
    return principal * rate * time / 100
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time in years: "))
print("Simple interest =", simple_interest(p, r, t))
