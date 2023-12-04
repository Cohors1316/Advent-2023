import os
import re


file = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
puzzle = file.read().splitlines()
file.close()


class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __init__(self, string: str):
        data = re.findall(r"((\d+)\s+(\w+))", string)
        for item in data:
            setattr(self, item[2], int(item[1]))


class Game:
    number: int
    rounds: list[Round]

    def __init__(self, string: str):
        game, rounds = string.split(":")
        self.number = int(re.search(r"\d+", game).group(0))
        self.rounds = [Round(round) for round in rounds.split(";")]

    def within_limit(self, red: int, green: int, blue: int) -> bool:
        for round in self.rounds:
            if round.red > red or round.green > green or round.blue > blue:
                return False
        return True

    def minimum_power(self) -> int:
        red, green, blue = 0, 0, 0
        for round in self.rounds:
            red = round.red if round.red > red else red
            green = round.green if round.green > green else green
            blue = round.blue if round.blue > blue else blue
        return red * green * blue


games = [
    game.number
    for line in puzzle
    if (game := Game(line)).within_limit(red=12, green=13, blue=14)
]
powers = [Game(line).minimum_power() for line in puzzle]
print(f"Part 1: {sum(games)}")
print(f"Part 2: {sum(powers)}")
