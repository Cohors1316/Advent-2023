import os
import re

file = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
puzzle = file.read().splitlines()
file.close()


def get_numbers(strings: list[str]) -> list[int]:
    return [
        int(re.findall(r"(\d)", string)[0] + re.findall(r"(\d)", string)[-1])
        for string in strings
    ]


def replace_words(puzzle: list[str]) -> list[str]:
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for line in range(len(puzzle)):
        for word in words:
            index = words.index(word)
            puzzle[line] = puzzle[line].replace(word, f"{word[0]}{index}{word[-1]}")
    return puzzle


numbers: list[int] = []

numbers = get_numbers(puzzle)
print("Part 1:", sum(numbers))

numbers = get_numbers(replace_words(puzzle))
print("Part 2:", sum(numbers))
