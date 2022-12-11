def get_number(lower_limit, upper_limit):
    number = int(input())
    while number < lower_limit or number > upper_limit:
        number = int(input("Invalid entry, try again: "))
    return number


def draw_rectangle(vertical_side, horizontal_side):
    for vertical in range(vertical_side):
        for horizontal in range(horizontal_side):
            print("*  ", end="")
        print()


def rectangle_info(side1, side2):
    return side1*side2, 2*(side1+side2), side1 == side2


def factorial(number):
    product = 1
    for multiplier in range(number, 1, -1):
        product *= multiplier
    return product


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


def show_menu():
    print("1. Draw rectangle")
    print("2. Calculate information of a rectangle")
    print("3. Calculate factorial")
    print("4. Calculate combination")
    print("0. Exit")


def main():
    exit_char = "n"
    while exit_char == "N" or exit_char == "n":
        show_menu()
        print("Enter your selection [0-4]: ", end="")
        selection = get_number(0, 4)

        if selection == 1:
            print("Enter the vertical side length of the rectangle [1-20]: ", end="")
            vertical_side = get_number(1, 20)
            print("Enter the horizontal side lenght of the rectangle [1-75]", end="")
            horizontal_side = get_number(1, 75)
            draw_rectangle(vertical_side, horizontal_side)

        elif selection == 2:
            print("Enter side A [1-1000]: ", end="")
            sidea = get_number(1, 1000)
            print("Enter side B [1-1000]: ", end="")
            sideb = get_number(1, 1000)
            area, perimeter, square = rectangle_info(sidea, sideb)
            print(f"Area of the rectangle: {area}\nPerimeter of the rectangle: {perimeter}")
            print(f"Is the rectangle a square?: {square}")

        elif selection == 3:
            print("Enter a number [0-10]: ", end="")
            number = get_number(0, 10)
            print(f"{number}! = {factorial(number)}")

        elif selection == 4:
            print("Enter the number n for the C(n,k) [1-10]: ", end="")
            n = get_number(1, 10)
            print(f"Enter the number k for the C(n,k) [1-{n}]: ", end="")
            k = get_number(1, n)
            print(f"C({n},{k})={combination(n, k):}")

        else:
            exit_char = input("Are you sure you want to exit? (y/Y, n/N): ")
            while exit_char not in ["y", "Y", "n", "N"]:
                exit_char = input("Are you sure you want to exit? (y/Y, n/N): ")


main()
