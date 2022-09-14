# File: KarelCheckerboard.py
# Name: Sergio Ley Languren

"""This program teaches Karel to draw a checkerboard using beepers."""

import karel
import turns

def checkerboard():
    """Draws a checkerboard pattern in beepers."""
    find_starting_point()
    write()
    
def find_starting_point():
    """Corrects Karel's position on the board"""
    while front_is_blocked():
        turn_left()

def write():
    """writes the checkerboard pattern"""
    while beepers_in_bag():
        write_beeper_line()
        turn_left()
        move()
        turn_left()
        write_beeper_line()
        turn_right()
        move()
        turn_right()


def write_beeper_line():
    """writes a beeeper line in a checkboard pattern"""
    while front_is_clear():
        put_beeper()
        move()
        move()