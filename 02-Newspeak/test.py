# File: test.py
# Author: Sergio Ley Languren

"""
Program to test Newspeak.py functions
"""

from Newspeak import negate, intensify, reinforce
from time import sleep


# Assertion Error class
class WordIncorrect(AssertionError):
    def __str__(self):
        return f'''Word Incorrect warning: {self.args[0]}'''


# negate function test 
word1 = "cold"

print(f"the word is {word1}. The expected result is: un{word1}")
sleep(1)
result = negate(word1)
print("Result:\n")
sleep(1)
print(result)
assert result == "uncold", WordIncorrect(f"{result} did not meet the expected result of: uncold")

# intensify function test
print(f"the word is {word1}. The expected result is: plus{word1}")
sleep(1)
result = intensify(word1)
print("Result:\n")
sleep(1)
print(result)
assert result == "pluscold", WordIncorrect(f"{result} did not meet the expected result of: pluscold")

# reinforce test
word2 = "good"
print("Test reinforce.1:\n")
sleep(1)
print(f"the word is {word1}. The expected result is: doubleplus{word1}")
sleep(1)
result = reinforce(intensify(word1))
print("Result:\n")
sleep(1)
print(result)
assert result == "doublepluscold", WordIncorrect(f"{result} did not meet the expected result of: doublepluscold")
sleep(1)
print("Test reinforce.2:\n")
sleep(1)
print(f"the word is {word2}. The expected result is: doubleplusun{word2}")
sleep(1)
result = reinforce(intensify(negate(word2)))
print("Result:\n")
sleep(1)
print(result)
assert result == "doubleplusungood", WordIncorrect(f"{result} did not meet the expected result of: doubleplusungood")
sleep(1)
print("test ran successfully")