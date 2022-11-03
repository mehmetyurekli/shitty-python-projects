"""
Write an algorithm to calculate the factorial of a number entered by the user.
"""
number = int(input("Enter number: "))
factorial = 1

for i in range(1, number+1):
    factorial *= i

print(factorial)
