from collections import defaultdict, Counter

# pairs = defaultdict()

initial, points = open("input.txt").read().split('\n\n')

pairs = {}
for line in points.split('\n'):
    s, end = line.split(' -> ')
    pairs[s] = end

C = Counter()
for i in range(len(initial)-1):
    C[initial[i]+initial[i+1]] += 1

# print(C)
# print(pairs)

for t in range(40):
    C2 = Counter()
    for k in C:
        C2[k[0] + pairs[k]] += C[k]
        C2[pairs[k] + k[1]] += C[k]
    C = C2


cf = Counter()
for k in C:
    cf[k[0]] += C[k]
cf[initial[-1]] += 1


max = max(cf.values())
min = min(cf.values())

print(max - min)
