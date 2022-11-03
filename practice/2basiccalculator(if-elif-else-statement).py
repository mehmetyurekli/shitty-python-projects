"""
Question: Write an algorithm that applies one of the 4 operations (+-*/)
to the 2 real numbers entered by the user and prints the result on the screen.
"""
number1 = float(input("First number: "))
operator = input("Select an operator(+,-,/,*): ")
number2 = float(input("Second number: "))
if operator == "+":
    print(f"Result: {number1+number2}")
elif operator == "-":
    print(f"Result: {number1-number2}")
elif operator == "/":
    print(f"Result: {number1/number2}")
else:
    print(f"Result: {number1*number2}")