"""
Question: Write a function that takes a string from the user (morse code or english alphabet)
and converts it to the opposite one and prints. Letters can be upper or lower but
the morse code always returns upper letters. Space indicates end or start of a letter.
"""


def reverse_morse(dictionary):
    morse_to_eng = {}
    for key, value in dictionary.items():
        morse_to_eng[value] = key
    return morse_to_eng


ABC_TO_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ', ': '--..--', '.': '.-.-.-',
                '?': '..--..', '/': '-..-.', '-': '-....-',
                '(': '-.--.', ')': '-.--.-'}

MORSE_TO_ABC = reverse_morse(ABC_TO_MORSE)


def translate(message):
    operation = int(input("1. ABC to Morse\n2. Morse to ABC\nSelect an operation: "))
    if operation == 1:
        abc = True
    else:
        abc = False

    message_list = message.split()
    if abc:
        for word in message_list:
            for letter in word:
                letter = letter.upper()
                print(ABC_TO_MORSE[letter], end=" ")
            print(" ", end="")

    else:
        for word in message_list:
            print(MORSE_TO_ABC[word], end="")
        print(" ", end="")


message_test = "... . .-.. .- --  -- ..- .-. .- -"

translate(message_test)
