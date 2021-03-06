boarding_passes = open('puzzle5.txt').read().splitlines()

print("-----------Part 1-----------")
value = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

def rownum(row):
    binary = [value[data] for data in row]
    return int(''.join(binary), 2)

def colnum(col):
    binary = [value[data] for data in col]
    return int(''.join(binary), 2)

maxseat = 0
seats = []
for bpass in boarding_passes:
    seat = rownum(bpass[:7]) * 8 + colnum(bpass[7:])
    seats.append(seat)
    maxseat = max(seat, maxseat)
print(maxseat)

print("-----------Part 2-----------")
seats.sort()
i = 1
while i < len(seats):
    if seats[i] != seats[i - 1] + 1:
        print(seats[i] - 1)
        break
    i += 1
