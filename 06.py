"""https://adventofcode.com/2020/day/5"""


def get_answers_with_single_yes():
    with open(r'inputs/06.txt') as data:
        answers = ' '.join([line.strip() for line in data.readlines()]).split('  ')

    result = 0
    for answer in answers:
        result += len(set(answer.replace(' ', '')))
    return result


print(get_answers_with_single_yes())


def get_answers_with_all_yes():
    with open(r'inputs/06.txt') as data:
        answers = [l.split() for l in ' '.join([line.strip() for line in data.readlines()]).split('  ')]

    result = 0
    for answer in answers:
        result += len(set.intersection(*map(set, answer)))
    return result


print(get_answers_with_all_yes())
