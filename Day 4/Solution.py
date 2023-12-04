import re
import os

file = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
puzzle = file.read().splitlines()
file.close()


class Card:
    number: int
    winners: list[int]
    