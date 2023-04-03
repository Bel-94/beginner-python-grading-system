# Initialize a variable to hold the total grade
total_grade = 0

# Initialize a variable to hold the number of subjects
num_subjects = 0

# Loop through the subjects
for i in range(1, 6):
    # Prompt the user for a grade
    grade = input("Enter the grade for subject {} (0-100): ".format(i))

    # Check if the input is valid
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            print("Invalid input! Grade should be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input! Grade should be a number.")
        continue

    # Add the grade to the total
    total_grade += grade
    num_subjects += 1

# Calculate the average grade
if num_subjects > 0:
    average_grade = total_grade / num_subjects
    print("Average grade: {:.2f}".format(average_grade))
else:
    print("No valid grades entered.")
