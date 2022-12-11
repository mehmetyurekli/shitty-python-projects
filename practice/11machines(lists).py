"""
Question: There are machines numbered 1-10 in a factory.
Write an algorithm that takes the monthly (30  days) production data of these machines
sorted by day number from the user and finds the monthly total production amount of each machine
and the monthly total production amount of the factory.
"""
machines = [0] * 10
for days in range(1, 31):
    for machine_index in range(0, 10):
        print(f"Enter the monthly production data of the {machine_index+1}. machine in day {days}: ", end="")
        machines[machine_index] += int(input())


for i in range(len(machines)):
    print(f"Monthly work of machine {i+1}: {machines[i]}")

