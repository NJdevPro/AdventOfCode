import itertools

print("-----------Part 1-----------")
groups, group  = [], []
for line in open("puzzle6.txt","r"):
    if line in ['\n', '\r\n']:
        groups.append(group)
        group = []
    else:
        group.append(line.strip())
groups.append(group)

def make_set(group):
    words = [list(word) for word in group]
    letters = list(itertools.chain(*words))
    return set(letters)

def count_group(group):
    return sum([len(make_set(group))])

print(sum([count_group(g) for g in groups]))

print("-----------Part 2-----------")

def count2_group(group):
    l = len(group)
    count = make_set(group)
    return sum([1 for x in count.values() if x == l])

print(sum([count2_group(g) for g in groups]))
