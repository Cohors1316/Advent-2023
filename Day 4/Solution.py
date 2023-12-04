import re
import os

file = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
puzzle = file.read().splitlines()
file.close()


class Card:
    number: int
    winners: list[int]
    numbers: list[int]

    def __init__(self, string: str):
        card, data = string.split(":")
        self.card = re.findall(r"\d+", card)
        data = data.split("|")
        self.winners = data[0].strip().split(" ")
        self.numbers = data[1].strip().split(" ")

    