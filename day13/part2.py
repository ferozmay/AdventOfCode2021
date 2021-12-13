from collections import defaultdict

with open("input.txt") as file:
    grid = {}
    for line in file:
        line = line.strip()
        if line and line[0] != 'f':
            x, y = [int(i) for i in line.split(',')]
            grid[(x, y)] = '#'
        elif line and line[0] == 'f':
            # var -> either x or y
            # pos -> where to fold along
            var, pos = line.split()[-1].split("=")
            pos = int(pos)
            new_grid = {}
            for (x, y) in grid:
                if var == 'x':
                    if x < pos:
                        new_grid[(x, y)] = '#'
                    else:
                        new_grid[(pos-(x-pos), y)] = '#'
                elif var == 'y':
                    if y < pos:
                        new_grid[(x, y)] = '#'
                    else:
                        new_grid[(x, pos-(y-pos))] = '#'
                grid = new_grid

xm = max([x for (x, y) in new_grid.keys()])
ym = max([y for (x, y) in new_grid.keys()])

# printing out the eight capital letters
for y in range(ym+1):
    for x in range(xm+1):
        if (x, y) in new_grid:
            print('#', end="")
        else:
            print(".", end="")
    print()
