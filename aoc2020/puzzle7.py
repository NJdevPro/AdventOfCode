import re

print("-----------Part 1-----------")
contains = {}
for line in open("puzzle7.txt","r"):
    color = re.match('(.+?) bags', line).group(1)
    contains[color] = re.findall('(\d+) (.+?) bag', line)

def find_parents(child):
    parents = set()
    [parents.add(k) for k,v in contains.items() if child in [color for number, color in v]]
    parents.discard(child) # prevent infinite recursion
    return parents

def get_roots(color, tree):
    parents = find_parents(color)
    if parents:
        tree |= parents
        for p in parents:
            get_roots(p, tree)
    return tree

ancestry = get_roots("shiny gold", set())
print(len(ancestry))

print("-----------Part 2-----------")
def count_children(color):
    count = 1
    for quantity, color in contains[color]:
        if color != 'other':
            count += quantity * count_children(color)
    return count

print(count_children("shiny gold")-1)
