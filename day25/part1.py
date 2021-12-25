
grid = [line.strip() for line in open("input.txt").read().split()]

rows = len(grid)
cols = len(grid[0])

ans = 0

while True:
    ans += 1
    step = False
    grid2 = [[grid[r][c] for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '>':
                if grid[r][(c+1) % cols] == '.':
                    step = True
                    grid2[r][(c+1) % cols] = '>'
                    grid2[r][c] = '.'
    grid3 = [[grid2[r][c] for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid2[r][c] == 'v' and grid2[(r+1) % rows][c] == '.':
                step = True
                grid3[(r+1) % rows][c] = 'v'
                grid3[r][c] = '.'
    if not step:
        print(ans)
        break

    grid = grid3

# for r in range(rows):
#     row = ''
#     for c in range(cols):
#         row += grid[r][c]
#     print(row)
