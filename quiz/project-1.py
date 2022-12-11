# function for getting numbers easier
def get_number(lower_limit):
    entry = int(input())
    while entry < lower_limit:
        entry = int(input("Invalid entry. Try again: "))
    return entry


# variables for base and defect weight detection
temp_base_weight = 0
temp_base_weight_2 = 0
defect_weight = 0
base_weight = 0

# taw counters
accepted_taws = 0
declined_taws = 0
heaviest_taw = 0
most_number_of_taws = 0
heaviest_number_of_taws = 0
most_number_weight = 0
max_weight_difference = 0

# box counters
declined_boxes = 0
all_equal_boxes = 0
one_lighter_boxes = 0
one_heavier_boxes = 0

# variables for some spesific statistics
lighter_differences = 0
heavier_differences = 0
lighter_percentages = 0
heavier_percentages = 0

# booleans
first_defect = False
defect_detect = False
get_base_difference = False     # a boolean to assign first difference and percentage to min and max.(only once)
permission = "y"                # sentinel of the while loop

while permission == "y" or permission == "Y":
    print("Enter number of taws in the box [10 or more]: ", end="")
    number_of_taws = get_number(10)

    for i in range(1, number_of_taws+1):
        print(f"Enter the weight of the {i}. taw: ", end="")
        taw_weight = get_number(0)

        if i == 1:
            base_weight = taw_weight    # temporary base
            continue

        if taw_weight != base_weight:
            if first_defect:
                if taw_weight == temp_base_weight_2 and i == 3:    # only works for the 3rd taw. A - B - B or A - B - A
                    defect_weight = base_weight                    # (A and B are different taw weights)
                    base_weight = taw_weight
                else:
                    print("Defect detected. Box declined.")
                    declined_boxes += 1
                    defect_detect = True
                    break
            else:
                first_defect = True
                defect_weight = taw_weight
                if i == 2:
                    temp_base_weight_2 = taw_weight     # if the second taw is different, program saves the second taw.

        else:
            base_weight = taw_weight
            # we have the base now

    if not defect_detect:
        if first_defect:
            difference = base_weight - defect_weight
            percentage = abs(difference) / base_weight * 100
            if not get_base_difference:                         # set first different taw to max and min diff/percentage
                min_weight_difference = difference
                max_weight_difference = difference
                max_percentage = percentage
                min_percentage = percentage
                get_base_difference = True                # set it to true, so it does it only for first different taw

            if abs(difference) >= abs(max_weight_difference):
                max_weight_difference = difference              # I keep the differences positive and negative
                max_percentage = percentage                     # to determine if they are heavier or lighter in the end

            if abs(difference) < abs(min_weight_difference):
                min_weight_difference = difference
                min_percentage = percentage

            if difference < 0:
                difference = abs(difference)
                one_heavier_boxes += 1
                heavier_differences += difference
                heavier_percentages += percentage
                print(f"One taw is %{percentage:.2f} heavier than the others.")
                print(f"Weight difference is: {difference}mg")
            else:
                one_lighter_boxes += 1
                lighter_differences += difference
                lighter_percentages += percentage
                print(f"One taw is %{percentage:.2f} lighter than the others.")
                print(f"Weight difference is: {difference}mg")

        else:
            if taw_weight > heaviest_taw:
                heaviest_taw = taw_weight
                heaviest_number_of_taws = number_of_taws
            if number_of_taws > most_number_of_taws:
                most_number_of_taws = number_of_taws
                most_number_weight = taw_weight
            all_equal_boxes += 1
            print("All the taws are at equal weight.")

        accepted_taws += number_of_taws

    else:
        declined_taws += number_of_taws

    first_defect = False                # resetting the booleans for the next box
    defect_detect = False
    permission = input("Do you want to add another box?[y/Y or n/N]: ")
    while permission not in ["y", "Y", "n", "N"]:
        permission = input("Do you want to add another box?[y/Y or n/N]: ")

accepted_boxes = all_equal_boxes + one_heavier_boxes + one_lighter_boxes
total_boxes = declined_boxes + accepted_boxes

defect_box_percentage = declined_boxes / total_boxes * 100

# percentages
all_equal_percentage = all_equal_boxes / accepted_boxes * 100
one_lighter_percentage = one_lighter_boxes / accepted_boxes * 100
one_heavier_percentage = one_heavier_boxes / accepted_boxes * 100

# averages of weight difference values and weight difference percentages
average_weight_difference_heavier = heavier_differences / one_heavier_boxes
average_weight_difference_percentage_heavier = heavier_percentages / one_heavier_boxes

average_weight_difference_lighter = lighter_differences / one_lighter_boxes
average_weight_difference_percentage_lighter = lighter_percentages / one_lighter_boxes

# prints
print(f"Number of boxes with manufacturing defects: {declined_boxes}")
print(f"Their percentage in all boxes: {defect_box_percentage:.2f}%")

print(f"Accepted taws: {accepted_taws}\nReturned taws: {declined_taws}")

print(f"Number of boxes in which all taws are of equal weight: {all_equal_boxes}")
print(f"Number of boxes in which 1 taw is heavier than the others: {one_heavier_boxes}")
print(f"Number of boxes in which 1 taw is lighter than the others: {one_lighter_boxes}")

print(f"Their percentages in boxes without manufacturing defects:")
print(f"All equal: {all_equal_percentage:.2f}%, "
      f"One heavier: {one_heavier_percentage:.2f}%, "
      f"One lighter: {one_lighter_percentage:.2f}%")

print(f"Averages of weight difference values (1 taw is heavier): {average_weight_difference_heavier:.2f}")
print(f"Averages of weight difference percentages (1 taw is heavier): "
      f"{average_weight_difference_percentage_heavier:.2f}%")

print(f"Averages of weight difference values (1 taw is lighter): {average_weight_difference_lighter:.2f}")
print(f"Averages of weight difference percentages (1 taw is lighter): "
      f"{average_weight_difference_percentage_lighter:.2f}%")

print(f"Among the all equal boxes, number of taws in the box with the largest number of taws: {most_number_of_taws}")
print(f"Weight of a taw in that box: {most_number_weight}")

print(f"Among the all equal boxes, number of taws in the box with the heaviest taws: {heaviest_number_of_taws}")
print(f"Weight of a taw in that box: {heaviest_taw}")

print(f"Statistics of the weight difference where the value of the difference is largest:")
print(f"The value: {abs(max_weight_difference)}")
print(f"Percentage: {max_percentage:.2f}%")
# I kept the difference positive/negative, so I can decide if they are lighter or heavier now.
if max_weight_difference > 0:
    print(f"Sign: Lighter")
else:
    print(f"Sign: Heavier")

print(f"Statistics of the weight difference where the value of the difference is smallest:")
print(f"The value: {abs(min_weight_difference)}")
print(f"Percentage: {abs(min_percentage):.2f}%")
# I kept the difference positive/negative, so I can decide if they are lighter or heavier now.
if min_weight_difference > 0:
    print(f"Sign: Lighter")
else:
    print(f"Sign: Heavier")
