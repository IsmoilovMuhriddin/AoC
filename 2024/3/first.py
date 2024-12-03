import re
import sys


def read_lines_until_empty():
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:  # Stop on empty line
            break
        yield stripped_line

def multiply(string):
    """mul(11,8)
    
    """
    content = string[4:-1]
    a, b = content.split(',')
    ans = int(a) * int(b)
    return ans

def count_muls(word):
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, word)
    ans = 0
    for word in matches:
        ans += multiply(word)
    return ans

def main():
    line_reader = read_lines_until_empty()
    ans = 0
    for line in line_reader:
        result = count_muls(line)
        ans += int(result)
    return ans


print("Part 1: ", main())
