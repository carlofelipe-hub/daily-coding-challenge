""# 🎯 Day 3 Challenge — FizzBuzz
# This script loops from 1 to 100 and prints:
# "Fizz" for multiples of 3,
# "Buzz" for multiples of 5,
# "FizzBuzz" for multiples of both 3 and 5,
# or the number itself if none of the above.

# Step 1: Loop through numbers from 1 to 100
for number in range(1, 101):  # range is exclusive of the last number, so it goes up to 100

    # Step 2: Check divisibility
    # First, check if it's divisible by both 3 and 5 (order matters here)
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # If not, check if it's divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # If not, check if it's divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If none of the above, just print the number
    else:
        print(number)
""
