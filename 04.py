import re

raw_passports = []
with open('inputs/04.txt') as file:
    data = file.readlines()
    string = ""
    for line in data:
        if line != '\n':
            string += line
        else:
            raw_passports.append(string.replace('\n', ' ').split())
            string = ''
    raw_passports.append(string.replace('\n', ' ').split())

passports = []
for p in raw_passports:
    data = {}
    for pair in p:
        key, val = pair.split(':')
        data[key] = val
    passports.append(data)


def check_height(string):
    unit = string[-2:]
    val = string[:-2]
    if unit == 'in' and int(val) in range(59, 77):
        return True
    if unit == 'cm' and int(val) in range(150, 194):
        return True
    else:
        return False


def check_range(val, min, max):
    return int(val) in range(min, max + 1)


def check_num(val):
    return val.isnumeric() and len(val) == 9


def check_color(string):
    return re.match(r'^#(?:[0-9a-fA-F]{6})$', string)


def check_eye_color(string):
    return string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


required_fields = {'byr': lambda val: check_range(val, 1920, 2002),
                   'iyr': lambda val: check_range(val, 2010, 2020),
                   'eyr': lambda val: check_range(val, 2020, 2030),
                   'hgt': lambda val: check_height(val),
                   'hcl': lambda val: check_color(val),
                   'ecl': lambda val: check_eye_color(val),
                   'pid': lambda val: check_num(val)}


def check_field(field, passport):
    return bool(
        required_fields[field](passport[field])) if field in passport else False


def check_passports_general():
    valid_passports = 0
    for passport in passports:
        valid_fields = 0
        for field in required_fields.keys():
            if field in passport:
                valid_fields += 1
        if valid_fields == 7:
            valid_passports += 1
    return valid_passports


def check_passports_detailed():
    valid_passports = 0
    for passport in passports:
        valid_fields = 0
        for field in required_fields.keys():
            valid_fields += check_field(field, passport)
        if valid_fields == 7:
            valid_passports += 1
    return valid_passports


print(check_passports_general())
print(check_passports_detailed())