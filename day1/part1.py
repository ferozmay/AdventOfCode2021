import re

with open("input1.txt", "r") as inp:

    data = inp.readlines()
    new_data = []
    for line in data:
        new_line = re.sub("\n", "", line)
        new_data.append(int(new_line))

    count = 0
    for i in range(1, len(new_data)):
        if new_data[i] > new_data[i-1]:
            count += 1

    print(count)
