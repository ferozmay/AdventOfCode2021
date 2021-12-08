from sys import maxsize

with open("input.txt") as file:
    crabs = [int(x) for x in file.read().strip().split(",")]

crabs.sort()

least = maxsize
for pos in range(crabs[-1]+1):
    fuel = 0
    for crab in crabs:
        diff = abs(crab-pos)
        fuel += (diff * (diff + 1)) // 2
    if fuel < least:
        least = fuel

print(least)
