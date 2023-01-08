"""
Question: Write an algorithm that finds whether a given text is palindrome or not.
"""


def if_palindrome(text):
    len_text = len(text)
    reversed_text = ""
    for i in range(len_text-1, -1, -1):
        reversed_text += text[i]

    if text == reversed_text:
        return True
    else:
        return False


def main():
    text = str(input("Enter a text: "))
    if if_palindrome(text):
        print("Palindrome")
    else:
        print("Not palindrome")


main()
