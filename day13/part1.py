
with open("input.txt") as file:
    grid = {}
    for line in file:
        line = line.strip()
        if line and line[0] != 'f':
            x, y = [int(i) for i in line.split(',')]
            grid[(x, y)] = '#'
        elif line and line[0] == 'f':

            new_grid = {}
            for (x, y) in grid:
                if x < 655:  # found this value at first fold
                    new_grid[x, y] = '#'
                else:
                    new_grid[(655-(x-655), y)] = '#'

            print(len(new_grid))
            break

# print(grid)
