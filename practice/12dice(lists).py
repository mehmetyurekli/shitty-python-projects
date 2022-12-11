"""
Question: Write an algorithm that takes the numbers from the user
as a result of rolling a backgammon dice 1000 times
and calculates how many times the numbers on the faces of the dice come,
the number that comes the most, and how many times this number comes.
"""
dice_sides = [0] * 6

for dice in range(10):
    result = int(input("Enter: "))
    while result < 0 or result > 6:
        result = int(input("Enter: "))

    dice_sides[result-1] += 1

for sides in range(6):
    print(f"{sides+1} was rolled {dice_sides[sides]} times")
    max_dice_index = dice_sides.index(max(dice_sides))
print(f"Maximum rolled side: {max_dice_index+1}, It was rolled {max(dice_sides)} times")