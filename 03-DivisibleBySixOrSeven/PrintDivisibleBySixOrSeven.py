# File: PrintDivisibleBySixOrSeven.py
# Name: your name

"""
This program prints the integers in the range between LOWER_LIMIT
up to but not including UPPER_LIMIT that are divisible by either
6 or 7 but not both.
"""

# Constants

LOWER_LIMIT = 1
UPPER_LIMIT = 100

divisible_by_6 = []
divisible_by_7 = []

def print_divisible_by_six_or_seven():
    """Prints the integers in the range divisible by 6 or 7 but not both."""
    for i in range(LOWER_LIMIT, UPPER_LIMIT+1):
        if i % 6 == 0 and i % 7 != 0:
            divisible_by_6.append(i)
        else:
            if i % 6 != 0 and i % 7 == 0:
                divisible_by_7.append(i)
    return divisible_by_6 + divisible_by_7

# Startup code

if __name__ == "__main__":
    r = print_divisible_by_six_or_seven()
    print(r)
