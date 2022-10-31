"""
Question: In a military school entrance exam,
the height threshold is 175 cm and the weight threshold is 75 kg for men;
the height threshold is 165 cm and the weight threshold is 65 kg for women.
Write an algorithm that takes the gender (m/M/f/F),
height and weight data of the candidate and determines whether or not he/she has won the exam.
"""
#constants
MAX_HEIGHT_MEN = 175
MAX_WEIGHT_MEN = 75
MAX_HEIGHT_WOMEN = 165
MAX_WEIGHT_WOMEN = 65

#process
gender = input("Gender(m/f): ")
if gender == "m" or gender == "M":
    height = int(input("Height: "))
    weight = int(input("Weight: "))
    if height > MAX_HEIGHT_MEN or weight > MAX_WEIGHT_MEN:
        print("You did not won.")
    else:
        print("You won.")
elif gender == "f" or gender == "F":
    height = int(input("Height: "))
    weight = int(input("Weight: "))
    if height > MAX_HEIGHT_WOMEN or weight > MAX_WEIGHT_WOMEN:
        print("You did not won.")
    else:
        print("You won.")

else:
    print("Gender Invalid.")