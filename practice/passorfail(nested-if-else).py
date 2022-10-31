"""
Question: If the average of two midterm exam grades of a course is at least 75,
the final exam is exempted, otherwise, if the sum of 40% of the average of two midterm exam grades
and 60% of the final exam grade is at least 50, the course is passed.
According to this, write an algorithm to determine whether a student has passed the course (and how).
"""
midterm_1 = int(input("First midterm: "))
midterm_2 = int(input("Second midterm: "))
midterm_avg = (midterm_1 + midterm_2)/2
if midterm_avg >= 75:
    print("Final exam is exempted. You passed.")

else:
    final = int(input("Final grade:"))
    total_grade = midterm_avg*0.4 + final*0.6
    if total_grade >= 50:
        print("You passed.")
    else:
        print("You failed.")