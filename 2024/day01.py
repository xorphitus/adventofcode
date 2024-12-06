import re
import sys

def parse(s):
    nums = re.split(r'\s+', s.strip())
    return [int(x) for x in nums]

def exec(lines):
    left, right = [], []
    for line in lines:
        l, r = parse(line)
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    size = len(left)
    sum = 0
    for i in range(size):
        l, r = left[i], right[i]
        diff = l - r
        if diff < 0:
            diff *= -1
        sum += diff
    return sum

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    answer = exec(sys.stdin)
    print(answer)
