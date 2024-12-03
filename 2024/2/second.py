import sys


def read_lines_until_empty():
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:  # Stop on empty line
            break
        yield stripped_line


def is_safe_numbers(arr):
    # do it in one go, no need to check twice.
    inc = 1
    dec = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            inc += 1
            if arr[i] - arr[i - 1] > 3:
                return False
        if arr[i] < arr[i - 1]:
            dec += 1
            if arr[i - 1] - arr[i] > 3:
                return False
        if arr[i] == arr[i - 1]:
            return False
    return inc == len(arr) or dec == len(arr)


def check_if_safeable(arr):
    res = is_safe_numbers(arr)
    if res:
        return 1
    for i in range(len(arr)):
        res = is_safe_numbers(arr[:i] + arr[i + 1 :])
        if res:
            return 1
    return 0


def main():
    line_reader = read_lines_until_empty()
    ans = 0
    for line in line_reader:
        result = check_if_safeable([int(x) for x in line.split()])
        ans += int(result)
    return ans


print("Part 2: ", main())
