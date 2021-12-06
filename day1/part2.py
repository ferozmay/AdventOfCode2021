import re

with open("input1.txt", "r") as inp:

    data = inp.readlines()
    new_data = []
    for line in data:
        new_line = re.sub("\n", "", line)
        new_data.append(int(new_line))

    three_measurement = []
    for i in range(len(new_data)-2):
        depth = new_data[i] + new_data[i+1] + new_data[i+2]
        three_measurement.append(depth)

    count = 0
    for j in range(1, len(three_measurement)):
        if three_measurement[j] > three_measurement[j-1]:
            count += 1

    print(count)
