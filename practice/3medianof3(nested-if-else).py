number_1 = input("first: ")
number_2 = input("second: ")
number_3 = input("third: ")

if number_1 > number_2:
    if number_3 > number_1:                 #3/1/2
        print("1")
    elif number_3 > number_2:               #1/3/2
        print("3")
    else:                                   #1/2/3
        print("2")

else:
    if number_3 > number_2:                 #3/2/1
        print("2")
    elif number_3 < number_1:               #2/1/3
        print("1")
    else:                                   #2/3/1
        print("3")