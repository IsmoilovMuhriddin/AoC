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
    if len(a) > 3 or len(b) > 3:
        return 0
    ans = int(a) * int(b)
    return ans

def find_occurance(word, pattern):
    matches = [(int(match.start()), match.group()) for match in re.finditer(pattern, word)]
    return matches


def count_muls(word, enabled = True):
    do = "do()"
    dont = "don't()"
    pattern_dos_donts = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = find_occurance(word, pattern_dos_donts)
    matches.sort()
    ans = 0
    
    for index, word in matches:
        if word == do:
            enabled = True
        elif word == dont:
            enabled = False
        else:
            if enabled:
                ans += multiply(word)
    return ans, enabled

def main():
    line_reader = read_lines_until_empty()
    ans = 0
    enabled = True
    for line in line_reader:
        result, enabled = count_muls(line, enabled)
        # print(result)
        ans += int(result)
    return ans


print("Part 2: ", main())
