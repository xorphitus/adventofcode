import re
import sys

def parse(s):
    nums = re.split(r'\s+', s.strip())
    return [int(x) for x in nums]

def exec(lines):
    total = 0
    for line in lines:
        safe = True
        prev = None
        increase = None
        for num in parse(line):
            if prev is None:
                prev = num
                continue
            diff = prev - num
            if diff == 0 or diff < -3 or diff > 3:
                safe = False
                break
            prev = num
            if increase is None:
                increase = diff > 0
            elif (increase and diff < 0) or (not increase and diff > 0):
                safe = False
                break
        if safe:
            total += 1
    return total

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    answer = exec(sys.stdin)
    print(answer)
