
with open("input.txt") as file:
    signal = [x.strip("\n").split("|") for x in file.readlines()]


count = 0
for x in signal:
    digits = x[1].split()
    for digit in digits:
        if len(digit) in [2, 3, 4, 7]:
            count += 1

print(count)
