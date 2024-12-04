import re
import sys

WORD = "XMAS"


def read_lines_until_empty():
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:  # Stop on empty line
            break
        yield stripped_line


def count_xmas(grid):
    def in_bounds(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def find_word(x, y, dx, dy):
        word = ""
        positions = []
        for _ in range(4):
            if in_bounds(x, y):
                word += grid[x][y]
                positions.append((x, y))
                x, y = x + dx, y + dy
            else:
                break
        return word == "XMAS"

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if find_word(x, y, dx, dy):
                    count += 1

    return count


def grid_search(grid, last_position, path):
    initial_x, initial_y = last_position
    n = len(path)
    if n == len(WORD):
        return 1, path

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]
    ans = 0
    all_paths = []

    for dx, dy in directions:
        next_letter = WORD[len(path)]
        x = initial_x + dx
        y = initial_y + dy

        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            continue  # Skip if out of bounds

        # Check if the next character matches the next letter in the word
        if grid[x][y] == next_letter:
            # If it matches, extend the path and continue the search
            new_path = path + [(x, y)]
            res, res_path = grid_search(grid, (x, y), new_path)
            if res:
                ans += res
                all_paths.append(res_path)

    return ans, all_paths


def main():
    line_reader = read_lines_until_empty()
    ans = 0
    x_positions = []
    grid = []
    row = 0
    for line in line_reader:
        arr = []
        for i, char in enumerate(line):
            if char == "X":
                x_positions.append((row, i))
            arr.append(char)
        grid.append(arr)
        row += 1
    ans = 0
    # for x, y in x_positions:
    #     count, path = grid_search(grid, (x, y), [(x, y)])
    #     ans += count
    #     print((x, y), count)
    ans = count_xmas(grid)
    return ans


print("Part 1: ", main())
