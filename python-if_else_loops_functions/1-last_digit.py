#!/usr/bin/python3
from contextlib import nullcontext
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    num = number % 10
    if num == 0:
        print(f"Last digit of {number * -1} is {num} and is 0")
    else:
        print(
            f"Last digit of {number * -1} is {num * -1} and is less than 6 and not 0")
else:
    num = number % 10
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num > 0 and num < 6:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
    elif num == 0:
        print(f"Last digit of {number * -1} is {num} and is 0")
