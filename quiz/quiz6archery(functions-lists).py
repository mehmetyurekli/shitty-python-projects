MIN_NUMBER_ARCHERS = 8
MIN_PTS = 5
MAX_PTS = 10
MISS_PTS = 0

def main():
    # Try-Except in case user enters str to an int(input)
    try:
        number_of_archers = int(input("Enter number of archers [Min: 8]: "))
        while number_of_archers < MIN_NUMBER_ARCHERS:                                    # need minimum 8 archers
            number_of_archers = int(input("Invalid! Enter number of archers [Min: 8]: "))
        # Creating lists
        archer_pts = [0] * number_of_archers
        x_count = [0] * number_of_archers
        ten_count = [0] * number_of_archers
        archer_names = ["test"] * number_of_archers
        for index in range(len(archer_names)):
            archer_names[index] = str(input(f"Enter name and surname of the archer number {index+1}: "))
        number_of_shots = int(input("Enter number of shots: "))
    except ValueError:
        print("Invalid entry!")
    else:
        pts_calculator(number_of_archers, number_of_shots, archer_pts, ten_count, x_count)
        print(archer_pts)
        print_sorter(number_of_archers, archer_names, archer_pts, ten_count, x_count)


# A function to enter data to lists.
def pts_calculator(number_of_archers, number_of_shots, archer_pts, ten_count, x_count):
    for i in range(number_of_shots):        # looping shot numbers
        for archer_index in range(number_of_archers):       # looping every player's points
            pts = int(input(f"[Shot {i+1}] - Archer {archer_index+1}: "))
            if pts != MISS_PTS:
                while pts < MIN_PTS or pts > MAX_PTS:
                    print("Points must be between 5-10.")
                    pts = int(input(f"[Shot {i + 1}] - Archer {archer_index + 1}: "))
            archer_pts[archer_index] += pts
            if pts == 10:
                ten_count[archer_index] += 1
                x_hit = input("Was it an 'X Shot'?(y,n): ")
                while x_hit not in ["y", "n"]:
                    x_hit = input("Was it an 'X Shot'?(y,n): ")
                if x_hit == "y":
                    x_count[archer_index] += 1


# A function to find the index of the top player
def max_index_finder(number_of_archers, archer_pts, ten_count, x_count):
    max_index = 0       # First archer is the leader by default
    # MOST IMPORTANT STAGE: DETERMINING THE MAX_INDEX
    for index in range(number_of_archers):
        if archer_pts[index] < archer_pts[max_index]:
            continue
        elif archer_pts[index] > archer_pts[max_index]:
            max_index = index
        else:
            if ten_count[index] > ten_count[max_index]:
                max_index = index
            elif ten_count[index] == ten_count[max_index] and x_count[index] > x_count[max_index]:
                max_index = index

    return max_index        # I will use it in the printing section


# A function to sort archers and print them in a list
def print_sorter(number_of_archers, archer_names, archer_pts, ten_count, x_count):
    # I used f string to make the print good-looking
    print(f"{'Rank':<10} {'Name-Surname':^25} {'Pts':^10} {'10-Count':^10} {'X-count':>10}")
    print(f"{'-----':<10} {'-------------':^25} {'----':^10} {'---------':^10} {'--------':>10}")
    for i in range(number_of_archers):
        max_index = max_index_finder(number_of_archers, archer_pts, ten_count, x_count)
        print(f"#{i+1:<10}", end="")
        print(f"{archer_names[max_index]:^25}", end="")
        print(f"{archer_pts[max_index]:^10}", end="")
        print(f"{ten_count[max_index]:^10}", end="")
        print(f"{x_count[max_index]:>10}")
        # Setting the max_index 's point value to -1 so the program won't select it max again.
        archer_pts[max_index] = -1


# Calling the main function
main()
