
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([int(x) for x in line.strip("\n")])

R = len(grid)
C = len(grid[0])
xc = [-1, 0, 1, 0]  # x coords of adjacent points
yc = [0, 1, 0, -1]  # y coords of adjacent points

ans = 0

for r in range(R):
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r+xc[d]
            cc = c+yc[d]

            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] <= grid[r][c]:
                ok = False
        if ok:
            ans += grid[r][c] + 1

print(ans)
