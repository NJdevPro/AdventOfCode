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

def gen_neighbors():
    neighbors = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                for l in (-1, 0, 1):
                    neighbors.append((i,j,k,l))
    neighbors.remove((0,0,0,0))
    return neighbors

def mutate(cube, x, y, z, w, xmax, ymax, zmax, wmax):
    active = 0
    for (i,j,k,l) in neighbors:
        if 0 <= x+i < xmax and 0 <= y+j < ymax and 0 <= z+k < zmax and 0 <= w+l < wmax:
            print(x,y,z,w)
            if cube[x+i][y+j][z+k][w+l] == '#':
                active += 1
    state = cube[x][y][z][w]
    if state == '#':
        if (active == 2 or active == 3):
            pass
        else:
            state = '.'
    elif state == '.' and active == 3:
        state = '#'
    return state

def make_hypercube(side):
    def make_empty_plane(side):
        plane = []
        for i in range(side):
            plane.append(list('.' * side))
        return plane

    def make_empty_cube(xx, yy, zz):
        cube = []
        for i in range(zz):
            cube.append(make_empty_plane(xx, yy))
        return cube

    hyperbox = []
    # make a box large enough for all iterations (be damned with perf)
    for i in range(int(side/2)):
        hyperbox.append(make_empty_cube(side, side, side))

    hyperbox.append(make_box(side))

    for i in range(int(side/2-1)):
        hyperbox.append(make_empty_cube(side, side, side))
    return hyperbox

def iterate(hypercube, mutated, n):
    xxx = len(hypercube[:][:][0])
    yyy = len(hypercube[:][0])
    zzz = len(hypercube[0])
    www = len(hypercube)
    print(xxx, yyy, zzz, www)
    count = 0
    for x in range(xxx):
        for y in range(yyy):
            for z in range(zzz):
                for w in range(www):
                    state = mutated[x][y][z][w] = mutate(hypercube, x,y,z,w, xxx,yyy,zzz, www)
                    if state == '#':
                        count += 1
    return n, count


hypercube = make_box(len(lines[0]) + (2*NITER))
# for z in range(len(hypercube)):
#     print(z, hypercube[z])
neighbors = gen_neighbors()
mutated = deepcopy(hypercube)
for n in range(NITER):
    print(iterate(hypercube, mutated, n))
    hypercube = deepcopy(mutated)