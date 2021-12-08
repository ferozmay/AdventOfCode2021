
with open("input.txt") as file:

    fish = [int(x) for x in file.readline().split(",")]

for day in range(80):
    for i in range(len(fish)):
        if fish[i] != 0:
            fish[i] -= 1
        else:
            fish[i] = 6
            fish.append(8)

print(len(fish))
