import sys

def parse(lines):
    area = []
    for line in lines:
        row = []
        for c in line:
            if c == '\n':
                break
            row.append(c)
        area.append(row)
    return area

def getAntennas(area):
    antennas = {}
    for i in range(len(area)):
        for j in range(len(area[0])):
            p = area[i][j]
            if p == '.':
                continue
            if p not in antennas:
                antennas[p] = []
            antennas[p].append([i, j])
    return antennas

def getAntinodes(antennas, height, width):
    pairs = []
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            pairs.append([antennas[i], antennas[j]])

    antinodes = []
    for pair in pairs:
        ai, aj = pair[0]
        bi, bj = pair[1]
        ci, cj, di, dj = -1, -1, -1, -1
        if ai < bi:
            diff = bi - ai
            ci = ai - diff
            di = bi + diff
            if aj < bj:
                diff = bj - aj
                cj = aj - diff
                dj = bj + diff
            else:
                diff = aj - bj
                cj = aj + diff
                dj = bj - diff
        else:
            diff = ai - bi
            ci = ai + diff
            di = bi - diff
            if aj < bj:
                diff = bj - aj
                cj = aj - diff
                dj = bj + diff
            else:
                diff = aj - bj
                cj = aj + diff
                dj = bj - diff
        if ci >= 0 and ci < height and cj >= 0 and cj < width:
            antinodes.append((ci, cj))
        if di >= 0 and di < height and dj >= 0 and dj < width:
            antinodes.append((di, dj))
    return antinodes

def exec(area):
    antennaGroups = getAntennas(area)
    antinodes = set()
    for antennas in antennaGroups.values():
        for a in getAntinodes(antennas, len(area), len(area[0])):
            antinodes.add(a)
    return len(antinodes)

# cat /path/to/input.txt | python day06.py
if __name__ == '__main__':
    area = parse(sys.stdin)
    answer = exec(area)
    print(answer)
