"""
guessing game. numbers are between 1-100.
output: up,down,congrats, number of guesses.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
number = random.randint(MIN_NUMBER, MAX_NUMBER)
guess = int(input("Enter a guess: "))
guess_count = 1

while number != guess:
    if guess < number:
        print("UP!")
    else:
        print("DOWN!")
    guess = int(input("Enter a guess: "))
    guess_count += 1

print("CONGRATULATIONS!")
print(f"Number of guesses: {guess_count}")
