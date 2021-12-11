from collections import defaultdict

with open("input.txt") as file:
    lines = [x.strip("\n").split("|") for x in file.readlines()]

digits = defaultdict(int)
positions = defaultdict(int)

final = []

for line in lines:
    before, after = line[0], line[1]

    before = before.split()
    after = after.split()

    for num in before:
        for alpha in num:
            digits[alpha] += 1

    for alpha in digits:
        if digits[alpha] == 9:
            positions['BR'] = alpha

        if digits[alpha] == 4:
            positions['BL'] = alpha

        if digits[alpha] == 6:
            positions['TL'] = alpha

    for num in before:
        if len(num) == 2:
            for alpha in num:
                if digits[alpha] != 9:
                    positions['TR'] = alpha

        if len(num) == 3:
            for alpha in num:
                if alpha not in positions.values():
                    positions['T'] = alpha

        if len(num) == 4:
            for alpha in num:
                if digits[alpha] == 7:
                    positions['M'] = alpha

    for alpha in digits:
        if alpha not in positions.values():
            positions['B'] = alpha

    value = ""
    for num in after:
        if len(num) == 2:
            value += "1"
        elif len(num) == 3:
            value += "7"
        elif len(num) == 4:
            value += "4"
        elif len(num) == 7:
            value += "8"

        elif len(num) == 5:
            if positions['BL'] in num:
                value += "2"
            elif positions['TL'] in num:
                value += "5"
            else:
                value += "3"
        elif len(num) == 6:
            if positions['M'] in num and positions['BL'] in num:
                value += "6"
            elif positions['M'] in num and positions['TR'] in num:
                value += "9"
            else:
                value += "0"

    final.append(value)
    print(dict(digits))
    digits.clear()
    positions.clear()

total = 0
for val in final:
    total += int(val)

print(total)
