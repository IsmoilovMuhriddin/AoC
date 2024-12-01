from collections import defaultdict
from heapq import heappop, heappush

import sys


def read_lines_until_empty():
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:  # Stop on empty line
            break
        yield stripped_line


def main():
    left = defaultdict(int)
    right = defaultdict(int)

    line_reader = read_lines_until_empty()
    for line in line_reader:
        first, second = map(int, line.split())
        left[first] += 1
        right[second] += 1

    ans = 0
    # print(left, right)
    for key in left.keys():
        ans += key *left[key]* right[key]
    return ans


print("Part 2: ", main())
