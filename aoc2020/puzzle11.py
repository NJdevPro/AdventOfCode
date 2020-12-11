import copy

lines =  open("puzzle11.txt","r").read().splitlines()

# Part 1
increments = [(-1, 0), (1,0), (0, -1), (0,1), (-1, -1), (-1, 1), (1,-1), (1,1)]

def count_adjacents(seats, i, j, move):
    return sum([move(seats, i, j, dx, dy) for (dx, dy) in increments])

# move like a chess king
def king(seats, i, j, inc_i, inc_j):
    i += inc_i
    j += inc_j
    if seats[i][j] == '#':
        return 1
    if seats[i][j] == 'L':
        return 0
    return 0

def iterate(seats, tolerance, move):
    new_seats = copy.deepcopy(seats)
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[0])-1):
            seat = seats[i][j]
            if seat == '#':
                c = count_adjacents(seats, i, j, move)
                if c >= tolerance:
                    new_seats[i][j] = 'L'
            elif seat == 'L':
                c = count_adjacents(seats, i, j, move)
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

def run(part, tolerance, move):
    print("---------- Part {} -----------".format(part))
    last_room = copy.deepcopy(seats)
    i=1
    while True:
        new_room = iterate(last_room, tolerance, move)
        #[print(j, sep='\n') for j in new_room]
        if new_room == last_room:
            print('iteration ', i - 1, ', occupied: ', occupied(last_room))
            break
        last_room = new_room
        i+=1

# Part 2
width = len(seats[0]) - 1
height = len(seats) - 1

# move like a chess queen
def queen(seats, i, j, inc_i, inc_j):
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

if __name__ == "__main__":
    run(1, 4, king)
    run(2, 5, queen)
