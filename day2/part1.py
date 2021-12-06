
with open("input1.txt", "r") as inp:

    data = inp.readline()
    horizontal = 0
    vertical = 0
    while data:
        line = data.split()
        if line[0] == "forward":
            horizontal += int(line[1])
        elif line[0] == "up":
            vertical -= int(line[1])
        elif line[0] == "down":
            vertical += int(line[1])

        data = inp.readline()

    pos = horizontal * vertical
    print(pos)
