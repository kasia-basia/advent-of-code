map = []
with open('inputs/03.txt') as file:
    data = file.readlines()
    for line in data:
        map.append(line.rstrip())

width = len(map[0])
height = len(map)


def check_slope(right, left):
    x = 0
    y = 0
    result = 0
    while y < height:
        if map[y][x] == '#':
            result += 1
        x = x + right if x + right < width else x + right - width
        y += left
    return result


slope1 = check_slope(1, 1)
slope2 = check_slope(3, 1)
slope3 = check_slope(5, 1)
slope4 = check_slope(7, 1)
slope5 = check_slope(1, 2)


def multiply(*args):
    result = 1
    for a in args:
        result *= a
    return result


print(multiply(slope1, slope2, slope3, slope4, slope5))
