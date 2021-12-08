
with open("input.txt") as file:
    crabs = [int(x) for x in file.read().strip().split(",")]

crabs.sort()
# middle is best position as it's equidistant from either side
middle = crabs[len(crabs)//2]

fuel = 0
for pos in crabs:
    if pos > middle:
        fuel += pos-middle
    elif pos < middle:
        fuel += middle-pos

print(fuel)
