import sys

WORD = "XMAS"


def read_lines_until_empty():
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:  # Stop on empty line
            break
        yield stripped_line


def count_xmas(grid):
    def find_x_mas(x, y):
        left, right, left_down, right_down = grid[x][y], grid[x][y+2], grid[x+2][y], grid[x+2][y+2]
        mid = grid[x+1][y+1]
        if mid == "A":
            if left == right and left_down == right_down and ((left =="M" and left_down == "S") or (left == "S" and left_down == "M")):
                return True
            elif left == left_down and right == right_down and ((left =="M" and right == "S") or (left == "S" and right == "M")):
                return True
            
        return False

    rows, cols = len(grid), len(grid[0])
    count = 0
    for x in range(rows-2):
        for y in range(cols-2):
            if find_x_mas(x, y):
                count += 1

    return count




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
    ans = count_xmas(grid)
    return ans


print("Part 1: ", main())
