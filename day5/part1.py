
with open("input.txt") as file:

    coords = [x.strip("\n").split(' -> ') for x in file.readlines()]

ocean = [[0 for i in range(1000)] for j in range(1000)]

for x in coords:
    temp = []
    for y in x:
        temp.extend(y.split(","))
    temp = list(map(int, temp))

    if temp[0] == temp[2]:
        if temp[3] > temp[1]:
            for i in range(temp[1], temp[3]+1):
                ocean[i][temp[0]] += 1
        else:
            for i in range(temp[3], temp[1]+1):
                ocean[i][temp[0]] += 1

    if temp[1] == temp[3]:
        if temp[2] > temp[0]:
            for i in range(temp[0], temp[2]+1):
                ocean[temp[1]][i] += 1
        else:
            for i in range(temp[2], temp[0]+1):
                ocean[temp[1]][i] += 1

count = 0
for l in ocean:
    for coord in l:
        if coord >= 2:
            count += 1

print(count)
