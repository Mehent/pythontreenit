
with open("C:/pythontreenit/puzzlet/aoc2020_8_input.txt", "r") as filu:
    instruction = filu.read().split('\n')
# instruction = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99','acc +1', 'jmp -4', 'acc +6']
accumulator = 0
indexes = []

def func(instructions,i):
    global accumulator
    global indexes
    # print(indexes)
    # print(i)
    # print(accumulator)
    if i in set(indexes):
        # return accumulator
        return False
    if i >= len(instructions):
        return accumulator
    # print(instructions[i])
    if 'acc' in instructions[i]:
        print('acc')
        accumulator += int(instructions[i].split()[1])
        # print(accumulator)
        indexes.append(i)
        return func(instructions,i+1)

    if 'jmp' in instructions[i]:
        a = int(instructions[i].split()[1])
        print('a on:')
        print(a)
        indexes.append(i)
        # return
        return func(instructions, i+a)
        # func(instructions,i+1)
    if 'nop' in instructions[i]:
        print('nop')
        indexes.append(i)
        return func(instructions,i+1)

def change(instructions, i):
    global indexes
    global accumulator
    r = False
    if i == len(instructions):
        return
    if 'jmp' in instructions[i]:
        instructions[i] = 'nop'+' '+instructions[i].split()[1]
        indexes = []
        accumulator = 0
        r = func(instructions, 0)
        instructions[i] = 'jmp'+' '+instructions[i].split()[1]
    if r:
        return r
    else:
        # print('indeksi täällä on:')
        # print(i)
        return change(instruction, i+1)
    
# print(func(instruction, 0))
print(change(instruction, 0))


