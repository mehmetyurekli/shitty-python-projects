# CONSTANTS
MAX_SETS = 5                # maximum sets can be played.
GAME_DECIDER_SET = 3        # if you win or lose 3 sets, game is over.

# IN-GAME VARIABLES
set_won = 0
set_lost = 0                # ingame set variables
ingame_total_set = 0

set_pts_won = 0
set_pts_lost = 0
ingame_total_pts_won = 0    # ingame point variables
ingame_total_pts_lost = 0
max_diff = 0

# OVERALL VARIABLES
overall_pts_won = 0         # overall point count
overall_pts_lost = 0

overall_matches_won = 0
overall_matches_lost = 0    # overall match counts
without_lose_match = 0
sets_5 = 0

set_count = 1  # for understandable printing. I counted in which set the user enters data

print_name = "Invalid"      # for maximum difference team name

total_match = int(input("Total matches: "))

# LOOP FOR EVERY MATCH PLAYED
for i in range(1, total_match+1):
    name = input("Enter team name: ")

    # LOOP FOR EVERY SINGLE SET IN A GAME
    while not ((set_won == GAME_DECIDER_SET and set_lost <= 2) or (set_won <= 2 and set_lost == GAME_DECIDER_SET)):
        set_pts_won = int(input(f"Points won in set {set_count}: "))
        set_pts_lost = int(input(f"Points lost in set {set_count}: "))
        if set_pts_won > set_pts_lost:
            set_won += 1
        else:
            set_lost += 1
        ingame_total_pts_won += set_pts_won
        ingame_total_pts_lost += set_pts_lost
        set_count += 1

    set_count = 1

    ingame_total_set = set_won + set_lost

    difference = abs(ingame_total_pts_won - ingame_total_pts_lost)

    if difference > max_diff:
        max_diff = difference
        print_name = name

    if set_won > set_lost:
        overall_matches_won += 1
        result_print = "WON"
    else:
        overall_matches_lost += 1
        result_print = "LOST"

    if set_won == 3 and set_lost == 0:
        without_lose_match += 1

    if set_won + set_lost == MAX_SETS:
        sets_5 += 1

    average_pts_won = ingame_total_pts_won / ingame_total_set
    average_pts_lost = ingame_total_pts_lost / ingame_total_set

    print(f"YOU {result_print} MATCH {i}!\n")
    print(f"Points won: {ingame_total_pts_won}")
    print(f"Points lost: {ingame_total_pts_lost}")
    print(f"Number of sets won: {set_won}")
    print(f"Number of sets lost: {set_lost}")
    print(f"Average points won per set: {average_pts_won}")
    print(f"Average points lost per set: {average_pts_lost}\n")

    # added a little break to inspect the current match results. It's not a sentinel.
    continue_match = input("Press enter to continue: ")

    overall_pts_won += ingame_total_pts_won
    overall_pts_lost += ingame_total_pts_lost

    # GIVE VALUE ZERO TO ALL IN-GAME VARIABLES FOR NEXT MATCH AFTER SUMMING THEM IN OVERALL VARIABLES
    set_won, set_lost = 0, 0
    set_pts_won, set_pts_lost = 0, 0
    ingame_total_pts_won, ingame_total_pts_lost = 0, 0
    ingame_total_set = 0

# OUTPUT CALCULATIONS
overall_matches = overall_matches_won + overall_pts_lost
average_pts_won_total = overall_pts_won / total_match
percentage_of_without_losing_set = without_lose_match / overall_matches_won * 100
percentage_of_5_sets = sets_5 / total_match * 100

# LAST PRINTS
print(f"Total number of points won: {overall_pts_won}")
print(f"Average of pts per match: {average_pts_won_total}\n")

print(f"Number of matches won: {overall_matches_won}")
print(f"Number of matches lost: {overall_matches_lost}\n")

print(f"Matches won without losing a set: {without_lose_match}")
print(f"Percentage of it in matches won: {percentage_of_without_losing_set:.2f}%\n")

print(f"Number of matches finished in 5 sets: {sets_5}")
print(f"Percentage of it in all matches: {percentage_of_5_sets:.2f}%\n")

print(f"Highest difference between points in a single match: {max_diff}")
print(f"Name of the team with the highest difference between points: {print_name}\n")
