"""Assignment 4 - Question 49
Create student marks module and use it.
Run this file directly in VS Code.
"""

# Companion module: student_marks.py
# It defines total_and_average(marks). See the companion module in this folder.
from student_marks import total_and_average
marks = [float(x) for x in input("Enter marks separated by spaces: ").split()]
print("Total and average:", total_and_average(marks))
