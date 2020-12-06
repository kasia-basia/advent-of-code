"""https://adventofcode.com/2020/day/5"""

def getAnswersWithOneYes():
    with open(r'inputs/06.txt') as data:
        answers = ' '.join([line.strip() for line in data.readlines()]).split('  ')

    result = 0
    for answer in answers:
        result += len(set(answer.replace(' ', '')))
    return result


print(getAnswersWithOneYes())

def getAnswersWithAllYes():
    with open(r'06.txt') as data:
        answers = [l.split() for l in ' '.join([line.strip() for line in data.readlines()]).split('  ')]

    result = 0
    for answer in answers:
        result += len(set.intersection(*[set(a) for a in answer]))
    return result

print(getAnswersWithAllYes())