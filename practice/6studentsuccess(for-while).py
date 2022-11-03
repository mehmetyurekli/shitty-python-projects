"""
Write an algorithm that takes the grades of all students enrolled in a course from the user (-1 for end of data)
and calculates the class GPA, the number of successful students (student grade must be at least 60 to pass the course),
and the percentage of successful students for the course.
"""

class_count = 0
class_successful = 0
class_total_grade = 0
grade = 0

while grade >= 0:
    grade = int(input("Enter grade: "))
    if grade >= 60 and grade >= 0:
        class_successful += 1
        class_total_grade += grade
        class_count += 1

percentage = class_successful / class_count * 100
GPA = class_total_grade / class_count

print(f"Class GPA: {GPA}")
print(f"Successful students: {class_successful}")
print(f"Success percentage: {percentage}")
