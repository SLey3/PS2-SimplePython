# File: Newspeak.py
# Name: Sergio Ley Languren

"""
This module defines several functions that implement several of the
standard prefixes used in the Newspeak language described in George
Orwell's novel 1984.
"""

def negate(word: str) -> str:
    """appplies "un" to given words"""
    result = "un" + word
    return result

def intensify(word: str) -> str:
    """applies "plus" to given words"""
    result = "plus" + word
    return result

def reinforce(word: str) -> str:
    """applies "double" to given words"""
    result = "double" + word
    return result