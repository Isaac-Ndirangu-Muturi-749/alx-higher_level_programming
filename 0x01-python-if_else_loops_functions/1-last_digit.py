#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the last digit
last_digit = number % 10

# Determine if the last digit is greater than 5, less than 6 and not 0
if last_digit > 5:
    status = "and is greater than 5"
elif last_digit == 0:
    status = "and is 0"
else:
    status = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {status}")
