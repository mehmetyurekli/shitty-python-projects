# constants
LOW = 10000
MID = 25000
LOW_RATE = 0.15
MID_RATE = 0.20
HIGH_RATE = 0.25

# total variables
total_tax = 0
total_gross = 0
net_total = 0

# counting variables
low_count = 0
mid_count = 0
high_count = 0
rich_count = 0
count = 0

# input
gross = float(input("Enter gross pay: "))

# salary classification and ++count inside a loop
while gross > 0:
    if gross <= LOW:
        tax = gross * LOW_RATE
        low_count += 1
    elif gross <= MID:
        tax = gross * MID_RATE
        mid_count += 1
    else:
        tax = gross * HIGH_RATE
        high_count += 1
        if gross > 50000:
            rich_count += 1
    count += 1
    net = gross - tax
    total_tax += tax
    total_gross += gross
    net_total += net
    print(f"Tax: {tax}\nNet salary: {net}")
    gross = float(input("Enter gross pay: "))

# if statements and prints to prevent division by zero.
if high_count > 0:
    rich_percentage = rich_count / high_count * 100
    print(f"Percentage of representative salary above 50.000 among high gross salary level: %{rich_percentage:.2f}")
if total_gross > 0:
    tax_percentage = total_tax / total_gross * 100
    print(f"Total tax: {total_tax}, Percentage of tax in total gross salary: %{tax_percentage:.2f}")
if count > 0:
    average_representative = net_total / count
    print(f"Average of all sales representatives net salary: {average_representative:.2f}")

print(f"Low: {low_count}, Mid: {mid_count}, High: {high_count}")
