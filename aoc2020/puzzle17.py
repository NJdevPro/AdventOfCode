import timing
from copy import deepcopy

lines =  open("puzzle17.txt","r").read().splitlines()

print('----------- Part 1 -----------')

NITER = 6

def gen_neighbors():
    neighbors = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                neighbors.append((i,j,k))
    neighbors.remove((0,0,0))
    return neighbors

def mutate(cube, x, y, z, xmax, ymax, zmax):
    active = 0
    for (i,j,k) in neighbors:
        if 0 <= x+i < xmax and 0 <= y+j < ymax and 0 <= z+k < zmax:
            if cube[x+i][y+j][z+k] == '#':
                active += 1
    state = cube[x][y][z]
    if state == '#':
        if (active == 2 or active == 3):
            pass
        else:
            state = '.'
    elif state == '.' and active == 3:
        state = '#'
    return state

cube = []
def make_box(side):
    def make_empty_plane(side):
        plane = []
        for i in range(side):
            plane.append(list('.' * side))
        return plane

    box, plane = [], []
    # make a box large enough for all iterations (be damned with perf)
    for i in range(int(side/2)):
        box.append(make_empty_plane(side))
    [plane.append(list('.' * side)) for i in range(NITER)]
    for row in lines:
        plane.append(list('.' * NITER + row + '.' * NITER))
    [plane.append(list('.' * side)) for i in range(NITER)]
    box.append(plane)
    for i in range(int(side/2-1)):
        box.append(make_empty_plane(side))
    return box

def iterate(cube, mutated, n):
    xxx = len(cube[:][0])
    yyy = len(cube[0])
    zzz = len(cube)
    count = 0
    for x in range(xxx):
        for y in range(yyy):
            for z in range(zzz):
                state = mutated[x][y][z] = mutate(cube, x,y,z,xxx,yyy,zzz)
                if state == '#':
                    count += 1
    return n, count


cube = make_box(len(lines[0]) + (2*NITER))
# for z in range(len(cube)):
#     print(z, cube[z])
neighbors = gen_neighbors()
mutated = deepcopy(cube)
for n in range(NITER):
    print(iterate(cube, mutated, n))
    cube = deepcopy(mutated)

print('----------- Part 2 -----------')

# Solution by Pataluc https://github.com/pataluc/AoC2020/blob/master/day17.py
import sys

actives = set()
actives4 = set()

for x, line in enumerate(lines):
    for y, cell in enumerate((line.rstrip())):
        if cell == '#':
            actives.add((x, y, 0))
            actives4.add((x, y, 0, 0))

def neighbours(x, y, z):
    return set((x + x_offset, y + y_offset, z + z_offset)
            for x_offset in range(-1, 2)
            for y_offset in range(-1, 2)
            for z_offset in range(-1, 2))

def neighbours4(x, y, z, w):
    return set((x + x_offset, y + y_offset, z + z_offset, w + w_offset)
            for x_offset in range(-1, 2)
            for y_offset in range(-1, 2)
            for z_offset in range(-1, 2)
            for w_offset in range(-1, 2))

def process(actives, neighbours_function):
    new_actives = set()
    for cell in set.union(*[neighbours_function(*cell) for cell in actives]):
        nb_active_neighours = len(actives & neighbours_function(*cell))
        if (cell not in new_actives
            and ((cell in actives and 3 <= nb_active_neighours <= 4)
            or (cell not in actives and nb_active_neighours == 3))):
            new_actives.add(cell)
    return new_actives

for i in range(6):
    print("Tour %d" % i)
    actives = process(actives, neighbours)
    actives4 = process(actives4, neighbours4)

print("ex1: %s" % len(actives))
print("ex2: %s" % len(actives4))
