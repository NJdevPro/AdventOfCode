import itertools as it
import copy

lines =  open("puzzle11.txt","r").read().splitlines()

print("---------- Part 1 -----------")
val = {'#':1, '.':0, 'L':0, 'X':0}
def count_adj(seat, i, j):
    TL = val[seat[i-1][j-1]]
    T = val[seat[i-1][j]]
    TR = val[seat[i-1][j+1]]
    L = val[seat[i][j-1]]
    R = val[seat[i][j+1]]
    BL = val[seat[i+1][j-1]]
    B = val[seat[i+1][j]]
    BR = val[seat[i+1][j+1]]
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
    return sum([row.count('#') for row in room])

empty_row = ['X'] * (len(lines[0]) + 2)
seats = []
seats.append(empty_row)
[seats.append(['X'] + list(line) + ['X']) for line in lines]
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

def count_adj2(seats, i, j):
    width = len(seats[0])-1
    height = len(seats)-1
    limit = min(width, height)

    def queen(m, n, inc_i, inc_j):
        i, j = m, n
        i += inc_i
        j += inc_j
        while (1 <= i <= height and 1 <= j <= width):
            if seats[i][j] == '#':
                return 1
            if seats[i][j] == 'L':
                return 0
            i += inc_i
            j += inc_j
        return 0

    T = queen(i, j, -1, 0)
    B = queen(i, j, +1, 0)
    L = queen(i, j, 0, -1)
    R = queen(i, j, 0, +1)
    TL = queen(i, j, -1, -1)
    TR = queen(i, j, -1, +1)
    BL = queen(i, j, +1, -1)
    BR = queen(i, j, +1, +1)
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
