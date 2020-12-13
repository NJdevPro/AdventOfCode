from operator import itemgetter

lines =  open("puzzle13.txt","r").read().splitlines()
departure = int(lines[0])
buses = [int(busID) for busID in lines[1].split(',') if busID != 'x']

# first method
minimum, idx = 1000000, 0
for n, busID in enumerate(buses):
    if busID != 'x':
        mod = busID - (departure % busID)
        if mod < minimum:
            minimum = mod
            idx = n
print(minimum, idx, minimum * buses[idx])

# second method
m = min(enumerate(map(lambda bus: bus - (departure % bus), buses)), key=itemgetter(1))
print(m[1], m[0], m[1] * buses[m[0]])


