"""Assignment 4 - Question 39
Modify global variable using global keyword.
Run this file directly in VS Code.
"""

count = 0
def increase():
    global count
    count += 1
increase()
print("Global count =", count)
