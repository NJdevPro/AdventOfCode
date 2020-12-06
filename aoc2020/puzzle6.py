import itertools
from collections import Counter

print("-----------Part 1-----------")
groups, group  = [], []
for line in open("puzzle6.txt","r"):
    if line in ['\n', '\r\n']:
        groups.append(group)
        group = []
    else:
        group.append(line.strip())
groups.append(group)

def count_group(group):
    words = [list(word) for word in group]
    letters = list(itertools.chain(*words))
    return sum([len(set(letters))])

print(sum([count_group(g) for g in groups]))

print("-----------Part 2-----------")

def count2_group(group):
    l = len(group)
    words = [list(word) for word in group]
    letters = list(itertools.chain(*words))
    count = Counter(letters)
    return sum([1 for x in count.values() if x == l])

print(sum([count2_group(g) for g in groups]))
