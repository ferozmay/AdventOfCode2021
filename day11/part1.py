

with open("input.txt") as file:
    lines = [list(map(int, line.strip("\n"))) for line in file.readlines()]


row = len(lines[0])
col = len(lines)

xc = [-1, -1, -1, 0, 1, 1, 1, 0]
yc = [-1, 0, 1, 1, 1, 0, -1, -1]

score = 0


def flashed(r, c):
    global score
    score += 1
    lines[r][c] = "_"  # to keep track of visited places
    for d in range(8):
        rr = r + xc[d]
        cc = c + yc[d]
        if 0 <= rr < row and 0 <= cc < col and lines[rr][cc] != "_":
            lines[rr][cc] += 1
            if lines[rr][cc] >= 10:
                flashed(rr, cc)


for i in range(100):
    for r in range(row):
        for c in range(col):
            lines[r][c] += 1
    for r in range(row):
        for c in range(col):
            if lines[r][c] == 10:
                flashed(r, c)
    for r in range(row):
        for c in range(col):
            if lines[r][c] == "_":
                lines[r][c] = 0

print(score)
