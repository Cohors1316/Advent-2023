import re
import os

file = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
puzzle = file.read().splitlines()
file.close()

# rather than checking if a number has a symbol, I'm going to instead search for symbols and find adjacent numbers

# This is no where near optimized, I was just trying to come up with a solution that worked


class Cell:
    row: int
    column: int
    value: str
    
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    @property
    def is_number(self) -> bool:
        return self.value.isnumeric()
        
    @property
    def is_gear(self) -> bool:
        return self.value == "*"
        
cells = [
    [
        Cell(row, column, value)
        for column in range(len(puzzle[0]))
        if (value := puzzle[row][column]) != "."
    ]
    for row in range(len(puzzle))
]

def adjacent_cells(cell: Cell, cells: list[Cell]) -> list[Cell]:
    pass

def is_symbol(row: int, column: int) -> bool:
    value = puzzle[row][column]
    if value.isnumeric() or value == ".":
        return False
    if value == "*":
        filtered[row][column] = "*"
    return True

def is_gear(row: int, column: int) -> bool:
    return puzzle[row][column] == "*"

def get_gear_ratio(field: tuple[int, int], table: list[str]) -> int:
    row, column = field
    table_2 = [[" " for i in range(len(table[0]))] for j in range(len(puzzle))]
    for r, c in adjacent_fields(row, column):
        if not table[r][c].isnumeric():
            continue
        table_2[r][c] = table[r][c]
        for i in range(c, -1, -1):
            if not table[r][i].isnumeric():
                break
            table_2[r][i] = table[r][i]
        for i in range(c, len(table[r])):
            if not table[r][i].isnumeric():
                break
            table_2[r][i] = table[r][i]
    gear_numbers: list[int] = []
    for r in table_2:
        numbers = re.findall(r"\d+", "".join(r))
        for number in numbers:
            gear_numbers.append(int(number))
    if len(gear_numbers) == 2:
        return gear_numbers[0] * gear_numbers[1]
   
def adjacent_fields(row: int, str: int) -> list[tuple[int, int]]:
    return [
        (row - 1, column - 1),
        (row - 1, column),
        (row - 1, column + 1),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column - 1),
        (row + 1, column),
        (row + 1, column + 1),
    ]


def get_numbers(field: tuple[int, int]) -> None:
    row, column = field
    if not puzzle[row][column].isnumeric():
        return
    filtered[row][column] = puzzle[row][column]
    for i in range(column, -1, -1):
        if not puzzle[row][i].isnumeric():
            break
        filtered[row][i] = puzzle[row][i]
    for i in range(column, len(puzzle[row])):
        if not puzzle[row][i].isnumeric():
            break
        filtered[row][i] = puzzle[row][i]

filtered = [[" " for i in range(len(puzzle[0]))] for j in range(len(puzzle))]

for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
        if not is_symbol(row, column):
            continue
        for field in adjacent_fields(row, column):
            get_numbers(field)

numbers: list[int] = []
for row in filtered:
    found = re.findall(r"\d+", "".join(row))
    if found:
        numbers.extend(found)
print("Part 1:", sum([int(i) for i in numbers]))

gear_ratios: list[int] = []
for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
        if not is_gear(row, column):
            continue
        ratio = get_gear_ratio((row, column,), puzzle.copy())
        if ratio:
            gear_ratios.append(ratio)
print("Part 2:", sum(gear_ratios))
