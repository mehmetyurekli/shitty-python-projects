# Problem:
# A private university gives a monthly scholarship of $250 to all its students. Also
# the university gives an additional scholarship to students with a GPA of at least 2 (out of 4), 35 times their GPA.
# In addition, the university gives an additional $150 to female students whose family income is below the minimum wage ($2400).
# According to this, write an algorithm and a program that takes the name, surname, GPA (out of 4)
# and gender (m/f) data of a student, and if it is a girl, the monthly income of her family
# from the user (no error checking needed) and calculates the monthly scholarship amount
# that the student will receive and prints it on the screen.


STANDART_SCHOLAR = 250
MINIMUM_WAGE = 2400

name = str(input("Name and surname: "))
gpa = float(input("GPA: "))
gender = str(input("Gender(m/f): "))
total_scholar = 250

if gender == "f":
    wage = float(input("Enter your family's monthly income: "))

if gender == "f" and wage < 2400:
    total_scholar = total_scholar + 150

if gpa >= 2:
    total_scholar = total_scholar + (gpa * 35)

print(f"Total Scholarship: {total_scholar}")