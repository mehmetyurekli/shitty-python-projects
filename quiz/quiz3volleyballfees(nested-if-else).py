# constant and first inputs
LEAGUE_MATCH = 26
age = int(input("Enter your age: "))
last_fee = float(input("Enter your last annual fee ($): "))
rank = int(input("Enter your team's rank at the end of the regular season: "))

# check the age and calculate release fee if the player has the right to leave.
if age == 22:
    release_fee = last_fee * 2
    release_accept = 1
elif age == 23:
    release_fee = last_fee
    release_accept = 1
elif age == 24:
    release_fee = last_fee/2
    release_accept = 1
elif age < 22:
    release_fee = 0
    release_accept = 0
else:
    release_fee = 0
    release_accept = 1

# calculate the cost if the team was at playoffs + print
if rank <= 8:
    playoff = int(input("Playoff: "))
    cost = last_fee / (LEAGUE_MATCH + playoff)
    if release_accept == 1:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: {release_fee:.2f}")
    else:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You do not have the right to be released (leave your team).")

# calculate the cost if the team wasn't at playoffs + print
else:
    cost = last_fee / LEAGUE_MATCH
    if release_accept == 1:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You have the right to be released (leave your team), your release fee: {release_fee:.2f}")
    else:
        print(f"Your cost to your team per game you play: {cost:.2f}")
        print(f"You do not have the right to be released (leave your team).")
