#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number % 10) if number >= 0 else ((number * -1) % 10)
text = "Last digit of"
if last_digit > 5:
    print(f"{text} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{text} {number} is {last_digit} and is 0")
else:
    print(f"{text} {number} is {last_digit} and is less than 6 and not 0")