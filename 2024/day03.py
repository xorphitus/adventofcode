import sys

# Challenge without regexp

expr = 'mul('

nums = set()
for i in range(10):
    nums.add(str(i))

def starts(s):
    ret = []
    offset = 0
    while True:
        idx = s.find(expr, offset)
        if idx < 0:
            break
        idx = idx + len(expr)
        ret.append(idx)
        offset = idx

    return ret

def args(s, offset):
    size = len(s)
    argL, argR = '0', '0'
    isL = True
    close = False
    for i in range(offset, size):
        c = s[i]
        if c in nums:
            if isL:
                argL += c
            else:
                argR += c
        elif c == ',' and isL:
            isL = False
        elif c == ')' and not isL:
            close = True
            break
        else:
            break
    if close:
        return int(argL), int(argR)
    else:
        return 0, 0

def exec(lines):
    total = 0
    for line in lines:
        arg0 = 0
        arg1 = 0
        for idx in starts(line):
            arg0, arg1 = args(line, idx)
            total += arg0 * arg1
    return total

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    answer = exec(sys.stdin)
    print(answer)
