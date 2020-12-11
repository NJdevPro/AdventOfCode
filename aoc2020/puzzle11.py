import itertools as it
import copy

lines =  open("puzzle11.txt","r").read().splitlines()

# Part 1
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

def iterate(seats, tolerance, count_adjacent):
    new_seats = copy.deepcopy(seats)
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[0])-1):
            seat = seats[i][j]
            if seat == '#':
                c = count_adjacent(seats, i, j)
                if c >= tolerance:
                    new_seats[i][j] = 'L'
            elif seat == 'L':
                c = count_adjacent(seats, i, j)
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

def run(part, tolerance, count_adjacence):
    print("---------- Part {} -----------".format(part))
    last_room = copy.deepcopy(seats)
    i=1
    while True:
        new_room = iterate(last_room, tolerance, count_adjacence)
        #[print(j, sep='\n') for j in new_room]
        if new_room == last_room:
            print('iteration ', i - 1, ', occupied: ', occupied(last_room))
            break
        last_room = new_room
        i+=1

# Part 2
increments = [(-1, 0), (1,0), (0, -1), (0,1), (-1, -1), (-1, 1), (1,-1), (1,1)]
width = len(seats[0]) - 1
height = len(seats) - 1

def count_adj2(seats, i, j):
    def queen(i, j, inc_i, inc_j):
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
    return sum([queen(i, j, dx, dy) for (dx, dy) in increments])

if __name__ == "__main__":
    run(1, 4, count_adj)
    run(2, 5, count_adj2)
