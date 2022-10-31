id = input("Enter student id: ")
name_surname = input("Enter name and surname: ")

theoretical_1 = float(input("Enter weekly theoretical course hours of the first course: "))
practical_1 = float(input("Enter weekly practical course hours of the first course: "))
ects_1 = float(input("Enter ECTS credits of the first course: "))
termgrade_1 = float(input("Enter term grade of the first course: "))

theoretical_2 = float(input("Enter weekly theoretical course hours of the second course: "))
practical_2 = float(input("Enter weekly practical course hours of the second course: "))
ects_2 = float(input("Enter ECTS credits of the second course: "))
termgrade_2 = float(input("Enter term grade of the second course: "))

localcredit_1 = theoretical_1 + (practical_1 / 2)
localcredit_2 = theoretical_2 + (practical_2 / 2)

total_credit = localcredit_1 + localcredit_2
total_ects = ects_1 + ects_2

wgpa_local = (localcredit_1 * termgrade_1 + localcredit_2 * termgrade_2) / total_credit
wgpa_ects = (ects_1 * termgrade_1 + ects_2 * termgrade_2) / total_ects

print(f"Student id: {id}\nName and surname: {name_surname}")
print(f"Total amount of local credits taken this semester: {total_credit:.2f}\nTotal amount of ECTS at the end of this semester: {total_ects:.2f}")
print(f"WGPA based on local credit at the end of this semester: {wgpa_local:.2f}")
print(f"WGPA based on ECTS at the end of this semester: {wgpa_ects:.2f}")