
with open("input1.txt", "r") as inp:

    data = inp.readline()

    horizontal = 0
    vertical = 0
    aim = 0

    while data:
        line = data.split()
        if line[0] == "forward":
            horizontal += int(line[1])
            vertical += (aim * int(line[1]))
        elif line[0] == "up":
            aim -= int(line[1])
        elif line[0] == "down":
            aim += int(line[1])

        data = inp.readline()

    pos = horizontal * vertical
    print(pos)
