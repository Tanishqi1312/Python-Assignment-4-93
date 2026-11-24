def total_and_average(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average
