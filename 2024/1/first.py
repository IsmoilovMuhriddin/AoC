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
    # read input
    left = []
    right = []
    line_reader = read_lines_until_empty()
    for line in line_reader:
        first, second = map(int, line.split())
        heappush(left, first)
        heappush(right, second)

    ans = 0
    while left:
        first, second = heappop(left), heappop(right)

        diff = abs(first - second)
        ans += diff
        # print(first, second, diff, ans)
    # print result
    # print("Part 1 answer:", ans)
    return ans


print("Part 1: ", main())
