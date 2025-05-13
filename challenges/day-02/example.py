""# 🎯 Day 2 Challenge — Simple Calculator
# This script accepts two numbers and an arithmetic operator,
# then performs the calculation and displays the result.

# Step 1: Get user inputs
# We use the input() function to get two numbers and an operator
try:
    num1 = float(input("Enter first number: "))  # Convert input to a float
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Step 2: Perform the calculation based on the operator
    if operator == '+':
        print(f"Result: {num1 + num2}")
    elif operator == '-':
        print(f"Result: {num1 - num2}")
    elif operator == '*':
        print(f"Result: {num1 * num2}")
    elif operator == '/':
        # Step 3: Handle division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        # If the operator is not valid
        print("Invalid Operator")

# Step 4: Handle invalid inputs (non-numeric values)
except ValueError:
    print("Invalid Input")
""
