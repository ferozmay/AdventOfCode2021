
with open("input1.txt", "r") as inp:

    data = inp.readlines()

    # dig1, dig2, dig3, dig4, dig5 = 0, 0, 0, 0, 0
    l = [0] * len(data[0])
    gamma = ""
    epsilon = ""

    for line in data:
        for i in range(len(line)):
            if line[i] == '0':
                l[i] += 1

    for i in range(len(line)):
        if l[i] > len(data)//2:
            gamma += "0"
        else:
            gamma += "1"

    for num in gamma:
        if num == "0":
            epsilon += '1'
        else:
            epsilon += '0'

    power = int(gamma, 2) * int(epsilon, 2)
    print(power)
