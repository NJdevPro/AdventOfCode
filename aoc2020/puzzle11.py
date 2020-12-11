import itertools as it
import copy

lines =  open("puzzle11.txt","r").read().splitlines()

print("---------- Part 1 -----------")
cc = {'#':1, '.':0, 'L':0}
def count_adj(c, i, j):
    TL = cc[c[i-1][j-1]]
    T = cc[c[i-1][j]]
    TR = cc[c[i-1][j+1]]
    L = cc[c[i][j-1]]
    R = cc[c[i][j+1]]
    BL = cc[c[i+1][j-1]]
    B = cc[c[i+1][j]]
    BR = cc[c[i+1][j+1]]
    return TL + T + TR + L + R + BL + B + BR

def iterate(seats, tolerance):
    new_seats = copy.deepcopy(seats)
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[0])-1):
            seat = seats[i][j]
            if seat == '#':
                c = count_adj(seats, i, j)
                if c >= tolerance:
                    new_seats[i][j] = 'L'
            elif seat == 'L':
                c = count_adj(seats, i, j)
                if c == 0:
                    new_seats[i][j] = '#'
    return new_seats

def occupied(room):
    c = 0
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[0])-1):
            if room[i][j] == '#':
                c+=1
    return c

empty_row = ['.']*(len(lines[0])+2)
seats = []
seats.append(empty_row)
for j,line in enumerate(lines):
    seats.append(['.'] + list(line) + ['.'])
seats.append(empty_row[:])

# last_room = copy.deepcopy(seats)
# i=1
# while True:
#     new_room = iterate(last_room, 4)
#     #[print(j, sep='\n') for j in new_room]
#     if new_room == last_room:
#         print('iteration ', i - 1, ', occupied: ', occupied(last_room))
#         break
#     last_room = new_room
#     i+=1

print("---------- Part 2 -----------")

# "I moved on her like a chess queen" / Ronald J. Frump
def queen(seat, m, n, inc_i, inc_j, limit_m, limit_n):
    i, j = m, n
    i += inc_i
    j += inc_j
    while ( 1 <= i <= limit_m and 1 <= j <= limit_n ):
        if seat[i][j] == '#':
            return 1
        if  seat[i][j] == 'L':
            return 0
        i += inc_i
        j += inc_j
    return 0

def count_adj2(seats, i, j):
    width = len(seats[0])-1
    height = len(seats)-1
    limit = min(width, height)
    T = queen(seats, i, j, -1, 0, height, width)
    B = queen(seats, i, j, +1, 0, height, width)
    L = queen(seats, i, j, 0, -1, height, width)
    R = queen(seats, i, j, 0, +1, height, width)
    TL = queen(seats, i, j, -1, -1, limit, limit)
    TR = queen(seats, i, j, -1, +1, limit, limit)
    BL = queen(seats, i, j, +1, -1, limit, limit)
    BR = queen(seats, i, j, +1, +1, limit, limit)
    return TL + T + TR + L + R + BL + B + BR

def iterate2(seats, tolerance):
    new_seats = copy.deepcopy(seats)
    width = len(seats[0])-1
    height = len(seats)-1
    for i in range(1, height):
        for j in range(1, width):
            seat = seats[i][j]
            if seat == '#':
                c = count_adj2(seats, i, j)
                if c >= tolerance:
                    new_seats[i][j] = 'L'
            elif seat == 'L':
                c = count_adj2(seats, i, j)
                if c == 0:
                    new_seats[i][j] = '#'
    return new_seats

last_room = copy.deepcopy(seats)
i=1
saved = {}
while True:
    new_room = iterate2(last_room, 5)
    #[print(j, sep='\n') for j in new_room]
    if new_room == last_room:
        print('iteration ', i - 1, ', occupied: ', occupied(new_room))
        break
    last_room = new_room
    i+=1