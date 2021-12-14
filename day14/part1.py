from collections import defaultdict, Counter

pairs = defaultdict()

for line in open("input.txt"):
    line = line.strip()
    if '->' not in line and line != "":
        temp = line
    elif line and line != "\n":
        k, v = line.split(" -> ")
        pairs[k] = v


for x in range(40):
    polymer = ""
    for i in range(len(temp)-1):
        key = temp[i] + temp[i+1]
        if key in pairs:
            polymer += key[0] + pairs[key]
        else:
            polymer += temp[i]
    polymer += temp[-1]
    temp = polymer

freq = Counter(polymer)
max = max(freq.values())
min = min(freq.values())

print(max - min)
