import copy


def transform_file():
    data = [line.strip().split(' ') for line in open("inputs/08.txt", "r")]
    return data


def update(line, curr):
    operation = line[0]
    value = int(line[1:])
    return curr + value if operation == '+' else curr - value


def execute_instruction(i, acc, instruction, num):
    if instruction == 'nop':
        i += 1
    if instruction == 'acc':
        acc = update(num, acc)
        i += 1
    if instruction == 'jmp':
        i = update(num, i)
    return i, acc


def run(code):
    acc = 0
    lines_visited = []
    i = 0
    while i < len(code):
        instruction, num = code[i]
        if i in lines_visited:
            # return acc # <== for part one
            return
        lines_visited.append(i)
        i, acc = execute_instruction(i, acc, instruction, num)
    print('Program successful', acc)
    return acc


def get_code_variations(code):
    result = [code]
    lines_to_change = [i for i, x in enumerate(code) if x[0] == 'jmp' or x[0] == 'nop']

    for line in lines_to_change:
        temp = copy.deepcopy(code)
        instruction = temp[line][0]
        if instruction == 'nop':
            temp[line][0] = 'jmp'
        elif instruction == 'jmp':
            temp[line][0] = 'nop'
        result.append(temp)

    return result


def test_variants(code_variants):
    for code in code_variants:
        run(code)


game_code = transform_file()
variants = get_code_variations(game_code)

print(run(game_code))
test_variants(variants)
