
from collections import defaultdict
from pprint import pprint

# _, target = open("input.txt").read().split(': ')

# tx, ty = target.split(", ")

# tx, ty = tx[2:].split(".."), ty[2:].split("..")
# len_tx = abs(int(tx[0]) - int(tx[1]))
# len_ty = abs(int(ty[0]) - int(ty[1]))

# corner1 = (int(tx[0]), int(ty[1]))
# corner2 = (int(tx[1]), int(ty[0]))

# print(corner1, corner2)
# topx = corner1[0]

# target_area = defaultdict()

# for x in range(len_tx):
#     for y in range(len_ty):
#         target_area[corner1[0]+x, corner1[1]+y] = 'T'

# pprint(target_area)

# target area: x=20..30, y=-10..-5
possible_max = []
count = 0
for X in range(300):
    for Y in range(-150, 150):
        lands_target_area = False
        x = 0
        y = 0
        maximum_y = 0
        now_x = X
        now_y = Y
        for t in range(500):
            x += now_x
            y += now_y
            maximum_y = max(maximum_y, y)
            if now_x > 0:
                now_x -= 1
            elif now_x < 0:
                now_x += 1
            now_y -= 1
            if 235 <= x <= 259 and -118 <= y <= -62:
                lands_target_area = True

        if lands_target_area:
            print(X, Y)
            count += 1
            possible_max.append(maximum_y)

print(max(possible_max))
print(count)
