"""
Question: Write an algorithm that takes the vendor name
and sales amount data from the user for each sale made by the vendors in a store
and calculates the total amount of the sales made by each vendor.
"""

vendor_names = {}

permission = "y"
while permission == "y":
    name = input("Enter vendor name: ")
    sale = int(input("Enter the sale amount: "))
    if name in vendor_names:
        vendor_names[name] += sale
    else:
        vendor_names[name] = sale
    permission = input("Do you want to continue?: ")

print(vendor_names)
