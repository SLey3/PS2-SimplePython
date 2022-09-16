# File: ListDivisibleBySixOrSeven.py

"""
This program tests the function list_divisible_by_six_or_seven,
which returns a list of the integers in range(lower, upper) that
are divisible by either 6 or 7 but not both.
"""

# Constants

LOWER_LIMIT = 1
UPPER_LIMIT = 100

def list_divisible_by_six_or_seven(lower, upper):
    """Returns a list of integers in range divisible by 6 or 7 but not both."""
    for i in range(lower, upper+1):
        if i % 6 == 0 and i % 7 != 0:
            print(f"{i} is divisible by only 6")
        else:
            if i % 6 != 0 and i % 7 == 0:
                print(f"{i} is divisble by only 7")

# Startup code

if __name__ == "__main__":
    list_divisible_by_six_or_seven(LOWER_LIMIT, UPPER_LIMIT)
