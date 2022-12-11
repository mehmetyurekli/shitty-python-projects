"""
Question: Write an algorithm that takes the foot size (37-46) and clothing size (50, 52, …, 60)
of each soldier in a military unit from the user and calculates how many boots of each size
and how many clothes of each size should be procured.
"""
foot_size = [0] * 10
cloth_size = [0] * 6
permission = "y"

try:
    while permission == "y" or permission == "Y":
        foot_input = int(input("Enter soldier's foot size[37-46]: "))
        while foot_input < 37 or foot_input > 46:
            foot_input = int(input("Enter soldier's foot size[37-46]: "))
        foot_index = (foot_input - 37)

        foot_size[foot_index] += 1

        cloth_input = int(input("Enter soldier's cloth size: "))
        while cloth_input < 50 or cloth_input > 60 or cloth_input % 2 != 0:
            cloth_input = int(input("Enter soldier's cloth size: "))
        cloth_index = int((cloth_input - 50) / 2)

        cloth_size[cloth_index] += 1

        permission = input("Do you want to continue?(y,Y or n,N): ")

except ValueError:
    print("Invalid enter")

else:
    print("BOOTS:")
    for foot in range(10):
        print(f"Size {37+foot}: {foot_size[foot]} boots.")
    print("CLOTHES:")
    for cloth in range(6):
        print(f"Size {50 + (cloth * 2)}: {cloth_size[cloth]} clothes.")