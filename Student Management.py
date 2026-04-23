# Name: Kaydan Venter
# Programming Assignment: Student Tuple Program
# Python Source File Name: K_Venter_Program1.py
# Program Description:
# This program asks the user to enter the name, grade, and student ID
# for five students. Each student's information is stored in a tuple,
# and all tuples are stored inside a list. The program then displays
# all student details and identifies the student with the highest
# and lowest grades.

# student_list: list that stores tuples containing student information
# student_tuple: tuple containing (name, grade, student ID)
# name: student's name
# grade: student's numeric grade
# student_id: student's ID number


# Function to get input for one student
def get_student():
    name = input("Enter student name: ")  # student's name
    grade = float(input("Enter student grade: "))  # student's grade
    student_id = input("Enter student ID: ")  # student's ID

    student_tuple = (name, grade, student_id)  # tuple storing student info
    return student_tuple


# Function to display all students
def display_students(student_list):
    print("\nStudent Details:")
    print("---------------------")

    for student in student_list:
        name = student[0]
        grade = student[1]
        student_id = student[2]

        print(f"Name: {name}, Grade: {grade}, ID: {student_id}")


# Function to find highest and lowest grade
def find_highest_lowest(student_list):

    highest = student_list[0]
    lowest = student_list[0]

    for student in student_list:
        if student[1] > highest[1]:
            highest = student

        if student[1] < lowest[1]:
            lowest = student

    print("\nHighest Grade:")
    print(f"Name: {highest[0]}, Grade: {highest[1]}, ID: {highest[2]}")

    print("\nLowest Grade:")
    print(f"Name: {lowest[0]}, Grade: {lowest[1]}, ID: {lowest[2]}")


# Main function
def main():

    student_list = []  # list that stores all student tuples

    print("Enter information for 5 students\n")

    for i in range(5):
        print(f"\nStudent {i+1}")
        student = get_student()
        student_list.append(student)

    display_students(student_list)

    find_highest_lowest(student_list)


# Run the program
main()
