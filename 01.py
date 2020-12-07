from itertools import combinations

values = []
with open('inputs/01.txt') as file:
    data = file.readlines()
    for line in data:
        values.append(int(line.rstrip()))

combos = list(combinations(values, 3))
for combo in combos:
    if sum(combo) == 2020:
        print(combo)
        print(combo[0] * combo[1] * combo[2])

