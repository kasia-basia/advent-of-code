"""https://adventofcode.com/2020/day/5"""

with open(r'05.txt') as data:
    codes = data.read().splitlines()


def calc_binary_space(str, maxVal):
    max = maxVal - 1
    min = 0
    for letter in str:
        diff = int(((max - min) + 1) / 2)
        if letter == '0':
            max -= diff
        if letter == '1':
            min += diff
    return min


def get_ids(codes):
    ids = []
    for code in codes:
        row = calc_binary_space(code[:7].replace('B', '1').replace('F', '0'), 128)
        col = calc_binary_space(code[-3:].replace('L', '0').replace('R', '1'), 8)
        seat_id = row * 8 + col
        ids.append(seat_id)
    return ids


def find_seat(seats):
    seats.sort()
    for (i, seat) in enumerate(seats):
        if seats[i + 1] - seat != 1:
            return seat + 1


ids = get_ids(codes)
print(max(ids))
print(find_seat(ids))
