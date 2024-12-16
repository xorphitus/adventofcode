import sys

def parse(lines):
    area = []
    for line in lines:
        row = []
        for c in line.strip():
            row.append(c)
        area.append(row)
    return area

def getStart(area):
    guard = set(['v', '<', '>', '^'])
    for i in range(len(area)):
        for j in range(len(area[0])):
            p = area[i][j]
            if p in guard:
                return i, j, p
    return -1, -1, ''

def count(area):
    count = 0
    for i in range(len(area)):
        for j in range(len(area[0])):
            if  area[i][j] == 'X':
                count += 1
    return count

def exec(area):
    i, j, d = getStart(area)
    prev = [i, j]
    rot = ''
    while i >= 0 and i < len(area) and j >= 0 and j < len(area[0]):
        if area[i][j] == '#':
            i, j = prev
            d = rot
        area[i][j] = 'X'
        prev = [i, j]
        rot = d
        if d == '<':
            j -= 1
            rot = '^'
        elif d == '>':
            j += 1
            rot = 'V'
        elif d == '^':
            i -= 1
            rot = '>'
        else:
            i += 1
            rot = '<'

    return count(area)

# cat /path/to/input.txt | python day06.py
if __name__ == '__main__':
    area = parse(sys.stdin)
    answer = exec(area)
    print(answer)
