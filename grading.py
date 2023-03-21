# Basic Grading System using Python Loops

# Ask user for input
score = int(input("Enter your score: "))

# Define grade ranges
grade_A = range(90, 101)
grade_B = range(80, 90)
grade_C = range(70, 80)
grade_D = range(60, 70)
grade_F = range(0, 60)

# Determine the grade based on score input
if score in grade_A:
    grade = "A"
elif score in grade_B:
    grade = "B"
elif score in grade_C:
    grade = "C"
elif score in grade_D:
    grade = "D"
elif score in grade_F:
    grade = "F"
else:
    print("Invalid input. Score should be between 0 and 100.")
    exit()

# Print the grade
print("Your grade is:", grade)
