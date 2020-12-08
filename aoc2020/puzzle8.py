import itertools
import re
import copy

instructions = []
for lines in open("puzzle8.txt","r").readlines():
    instructions.append([val.strip() for val in lines.split(' ')])
instructions0 = copy.deepcopy(instructions)

print("-----------Part 1-----------")

def exec(idx, instruction, acc):
    opcode, argument = instruction[0], int(instruction[1])
    if opcode == 'acc':
        acc += argument
        idx += 1
    elif opcode == 'jmp':
        idx += argument
    elif opcode == 'nop':
        idx += 1
    return idx, acc

idx, acc = 0, 0
loop = set()
while idx not in loop:
    loop.add(idx)
    idx, acc = exec(idx, instructions[idx], acc)
    #print(idx, opcode, ' ', argument, ' ', acc)
print(acc)

print("-----------Part 2-----------")
indexed_program = zip(range(len(instructions)), instructions)
list_of_nop_jmp = [inst[0] for inst in list(indexed_program) if inst[1][0] in ('nop', 'jmp')]

for index in list_of_nop_jmp:
    instructions = copy.deepcopy(instructions0)
    if instructions[index][0] == 'jmp':
        instructions[index][0] = 'nop'
    elif instructions[index][0] == 'nop':
        instructions[index][0] = 'jmp'

    idx, acc = 0, 0
    loop = set()
    while idx not in loop:
        if idx >= len(instructions):
            print(acc)
            exit()
        loop.add(idx)
        idx, acc = exec(idx, instructions[idx], acc)
