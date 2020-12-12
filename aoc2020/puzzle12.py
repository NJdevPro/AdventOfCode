import itertools as it

lines =  open("puzzle12.txt","r").read().splitlines()

print('----------- Part 1 -----------')
forward = {'N':0+1j, 'E':1+0j, 'S':0-1j, 'W':-1+0j}
directions = ['N', 'E', 'S', 'W']
right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}

pos = 0 + 0j
current_dir = 'E'

for step, instruction in enumerate(lines):
    instr = instruction[0]
    val = int(instruction[1:])
    if instr == 'F':
        pos += forward[current_dir] * val
    elif instr in directions:
        pos += forward[instr] * val
    elif instr == 'L':
        for i in range(int(val/90)):
            current_dir = left[current_dir]
    elif instr == 'R':
        for i in range(int(val/90)):
            current_dir = right[current_dir]

print(step + 1, pos)

print('----------- Part 2 -----------')
pos = 0+0j
wp = 10+1j

import cmath
Pi = 3.1415926535898
def add_90(pos):
    rho, phi = cmath.polar(pos)
    s = cmath.rect(rho, phi + Pi/2)
    real, im = round(s.real), round(s.imag)
    return real + im*(0+1j)

def sub_90(pos):
    rho, phi = cmath.polar(pos)
    s = cmath.rect(rho, phi - Pi/2)
    real, im = round(s.real), round(s.imag)
    return real + im*(0+1j)

for step, instruction in enumerate(lines):
    instr = instruction[0]
    val = int(instruction[1:])

    if instr == 'F':
        pos += wp * val
    elif instr in directions:
        wp += forward[instr] * val
    elif instr == 'L':
        for i in range(int(val/90)):
            wp = add_90(wp)
    elif instr == 'R':
        for i in range(int(val/90)):
            wp = sub_90(wp)

    print(step+1, instruction, pos, wp, pos.real + pos.imag)

print(step + 1, pos)