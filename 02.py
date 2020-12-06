"""https://adventofcode.com/2020/day/2"""


with open(r'02.txt') as data:
    passwords = [row.split(' ') for row in data.read().splitlines()]


def check_passwords1():
    i = 0
    for [times, letter, password] in passwords:
        min, max = times.split('-')
        if password.count(letter[0]) in range(int(min), int(max)+1):
            i = i+1
    return i


def check_passwords2():
    i = 0
    for [times, letter, password] in passwords:
        first, second = times.split('-')
        if bool(password[int(first)-1] == letter[0]) ^ bool(password[int(second)-1] == letter[0]):
            i += 1
    return i


print(check_passwords1())
print(check_passwords2())
