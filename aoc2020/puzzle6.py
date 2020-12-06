import itertools
from collections import Counter

lines = open("puzzle6.txt","r").readlines()

print("-----------Part 1-----------")
groups, group  = [], []
# had to add 2 empty lines at the end of the txt file else the count is off by 1
for line in lines:
    if line in ['\n', '\r\n']:
        groups.append(group)
        group = []
    else:
        group.append(line.strip())
groups.append(group)

def count_group(group):
    words = [list(word) for word in group]
    letters = list(itertools.chain(*words))
    c = Counter(letters)
    return sum([len(c.items())])

print(sum([count_group(g) for g in groups]))

print("-----------Part 2-----------")

def count2_group(group):
    l = len(group)
    words = [list(word) for word in group]
    letters = list(itertools.chain(*words))
    count = Counter(letters)
    s = sum([x == l for x in count.values()])
    return s

print(sum([count2_group(g) for g in groups]))