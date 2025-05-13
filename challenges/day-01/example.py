""# 🎯 Day 1 Challenge — Age Checker
# This script accepts the user's age and categorizes them as:
# Minor, Adult, or Senior Citizen.

# Step 1: Get user input
# We use the input() function to capture the user's age.
# It's wrapped in a try-except block to handle errors.
try:
    age = int(input("Enter your age: "))  # Convert the input to an integer
    
    # Step 2: Validate the age
    # If the age is negative, it's invalid
    if age < 0:
        print("Invalid Age")
    # If the age is less than 18, they're classified as a Minor
    elif age < 18:
        print("You are a Minor.")
    # If the age is between 18 and 60, they're an Adult
    elif 18 <= age <= 60:
        print("You are an Adult.")
    # If the age is above 60, they're a Senior Citizen
    else:
        print("You are a Senior Citizen.")

# Step 3: Handle invalid input (e.g., non-integer values)
except ValueError:
    print("Invalid Input")
""