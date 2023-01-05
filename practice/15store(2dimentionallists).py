"""
Question: In a store that is open every day of the week,
sales representatives are coded between 1 and 10.
Write an algorithm that takes the vendor code
and sales amount data of each sale made by the vendors for each day of the week
and calculates the daily and weekly sales totals of the vendors and the store's daily and weekly sales totals.
"""

# rows are for vendors and columns are for sales

rows, cols = (11, 8)    # one extra row and col to store total sales
value = 1
mylist = [[0 for i in range(cols)] for j in range(rows)]

store_total_sale = 0
permission = "y"

while permission == "y":
    vendor = int(input("Enter vendor id: "))
    row = vendor - 1
    for day in range(cols-1):
        sales = int(input(f"Enter day {day+1} sales: "))
        mylist[row][day] = sales
        mylist[rows-1][day] += sales        # daily totals
        mylist[row][cols-1] += sales        # vendors weekly total
    permission = input("Continue?: ")


for vendor_total in range(rows-1):
    print(f"Vendor {vendor_total+1}: ", end="")
    print(mylist[vendor_total][cols-1])

for daily_total in range(cols-1):
    print(f"Day {daily_total+1}", end="")
    store_day_sale = (mylist[rows-1][daily_total])
    print(store_day_sale)
    store_total_sale += store_day_sale

print(store_total_sale)

# some prints are missing because of my laziness
