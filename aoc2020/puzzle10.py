import itertools as it
from collections import Counter, defaultdict
adapters = [int(n) for n in open("puzzle10.txt", 'r').read().splitlines()]

print('----------- Part 1 -----------')
adapters.sort()
ad2 = adapters[1:]
differences = []
for i in range(len(ad2)):
    differences.append(ad2[i]-adapters[i])
print(differences)
c = Counter(differences)
print(c)
print((c[3]+1)*(c[1]+1))

print('----------- Part 2 -----------')
# couldn't do it