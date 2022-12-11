"""
Question: Write an algorithm that takes the grades (0-100) of students in a class from the user
and calculates the number of students in the grade ranges 0-9, 10-19, …, 80-89, 90-100.
"""
grade_ranges = [0] * 10
try:
    print(f" Enter the number of students: ", end="")
    number = int(input(""))
    for i in range(number):
        grade = int(input(f"Enter grade {i+1}: "))
        if grade == 100:
            grade_ranges[9] += 1
        else:
            grade_index = grade//10
            grade_ranges[grade_index] += 1

except ValueError:
    print("Invalid input!")

else:
    for index in range(len(grade_ranges)):
        lower_bound = index * 10
        upper_bound = lower_bound + 9
        if index == 9:
            upper_bound += 1
        print(f"{lower_bound} - {upper_bound} = {grade_ranges[index]}")
