from collections import defaultdict

with open("input.txt") as file:

    fish = [int(x) for x in file.readline().split(",")]

X = defaultdict(int)

for n in fish:
    if n not in X:
        X[n] = 0
    X[n] += 1

for day in range(256):
    new_X = defaultdict(int)
    for x, count in X.items():
        if x == 0:
            new_X[6] += count
            new_X[8] += count
        else:
            new_X[x-1] += count
    X = new_X

print(sum(X.values()))
