"""Assignment 4 - Question 38
Demonstrate local and global variables with same name.
Run this file directly in VS Code.
"""

value = "global"
def show():
    value = "local"
    print("Inside function:", value)
show()
print("Outside function:", value)
