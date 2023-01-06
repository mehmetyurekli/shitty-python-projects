"""
Question: The faces of a 6-sided dice are colored YELLOW, RED, BLUE, GREEN, PURPLE and ORANGE.
Write an algorithm that takes the colors from the user as a result of rolling this dice 1000 times
and calculates how many times the colors on the faces of the dice come.
"""

dictionary = {
    "yellow": 0,
    "red": 0,
    "blue": 0,
    "green": 0,
    "purple": 0,
    "orange": 0
}

for i in range(1000):
    side = str(input("Enter color: "))
    while side not in dictionary:
        side = str(input("Enter a valid color: "))

    dictionary[side] += 1

print(dictionary)
