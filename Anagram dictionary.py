# ------------------------------------------------------------
# Name: Kaydan Venter
# Programming Assignment: Student Scores
# File Name: K_Venter_Program1.py
# Program Description:
# This program prompts the user to enter the names and test scores
# of 10 students, stores them in a list, calculates the average score,
# and displays the highest and lowest scores along with the names
# of the students who achieved them.
# ------------------------------------------------------------

# Initialize an empty list to store student data (name and score)
students = []

# Input scores for 10 students
for i in range(10):
    name = input(f"Enter the name of student #{i + 1}: ")  # student's name
    score = float(input(f"Enter {name}'s test score: "))   # student's score
    students.append((name, score))  # store tuple of (name, score)

# Extract only scores into a separate list for calculations
scores = [s[1] for s in students]

# Calculate average score
average_score = sum(scores) / len(scores)

# Find highest and lowest scores
highest_score = max(scores)
lowest_score = min(scores)

# Identify students with highest and lowest scores
highest_students = [s[0] for s in students if s[1] == highest_score]
lowest_students = [s[0] for s in students if s[1] == lowest_score]

# Display results
print("\n--- Test Results Summary ---")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score} - Achieved by: {', '.join(highest_students)}")
print(f"Lowest Score: {lowest_score} - Achieved by: {', '.join(lowest_students)}")
