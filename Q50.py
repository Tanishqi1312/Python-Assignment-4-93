"""Assignment 4 - Question 50
Create a package with two modules and import functions from both.
Run this file directly in VS Code.
"""

# Package layout: student_package/__init__.py, basics.py, calculations.py
from student_package.basics import greet
from student_package.calculations import square
greet()
print("Square:", square(6))
