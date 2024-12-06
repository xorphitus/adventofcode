import sys
from collections import deque

def makeboard(stdin):
    board = []
    for line in stdin:
        row = [c for c in line]
        board.append(row)
    return board

def nextPosition(i, j, direction):
    i2, j2 = 0, 0
    if direction == 1:
        i2, j2 = i + 1, j - 1
    elif direction == 2:
        i2, j2 = i + 1, j
    elif direction == 3:
        i2, j2 = i + 1, j + 1
    elif direction == 4:
        i2, j2 = i, j - 1
    elif direction == 6:
        i2, j2 = i, j + 1
    elif direction == 7:
        i2, j2 = i - 1, j - 1
    elif direction == 8:
        i2, j2 = i - 1, j
    else:
        i2, j2 = i - 1, j + 1
    return i2, j2, direction

def exec(board):
    height = len(board)
    width = len(board[0])
    q = deque()
    for i in range(height):
        for j in range(width):
            c = board[i][j]
            if c == 'X':
                q.append([i, j, 5])
    total = 0
    while q:
        i, j, direction = q.popleft()
        c = board[i][j]
        nxt = ''
        if c == 'X':
            nxt = 'M'
        elif c == 'M':
            nxt = 'A'
        elif c == 'A':
            nxt = 'S'
        elif c == 'S':
            total += 1
            continue
        else:
            continue
        options = []
        if direction == 5:
            for k in range(1, 10):
                if k == 5:
                    continue
                i2, j2, d = nextPosition(i, j, k)
                options.append([i2, j2, d])
        else:
            i2, j2, d = nextPosition(i, j, direction)
            options.append([i2, j2, d])
        for i2, j2, d in options:
            if i2 >=0 and j2 >=0 and i2 < height and j2 < width and board[i2][j2] == nxt:
                q.append([i2, j2, d])
    return total

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    board = makeboard(sys.stdin)
    answer = exec(board)
    print(answer)
