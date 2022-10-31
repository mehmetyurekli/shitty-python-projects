team_1 = str(input("Enter the name of the first team: "))
sets_1 = int(input("Enter the number of sets won by the first team: "))
team_2 = str(input("Enter the name of the second team: "))
sets_2 = int(input("Enter the number of sets won by the second team: "))

if sets_1 == 3 and sets_2 == 1 or sets_2 == 0:
    winner = team_1
    loser = team_2
    ptsw = 3
    ptsl = 0

if sets_1 == 3 and sets_2 ==2:
    winner = team_1
    loser = team_2
    ptsw = 2
    ptsl = 1

if sets_2 == 3 and sets_1 == 1 or sets_1 == 0:
    winner = team_2
    loser = team_1
    ptsw = 3
    ptsl = 0

if sets_2 == 3 and sets_1 == 2:
    winner = team_2
    loser = team_1
    ptsw = 2
    ptsl = 1

print(f"The name of the team that won the match: {winner}, the points it earned: {ptsw}")
print(f"The name of the team that lost the match: {loser}, the points it earned: {ptsl}")
