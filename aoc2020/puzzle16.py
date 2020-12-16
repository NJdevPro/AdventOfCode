import timing
import re

lines =  open("puzzle16.txt","r").read().splitlines()

print('----------- Part 1 -----------')
number_of_rules = 20
my_ticket = 22
nearby_tickets = 25
rules = {}

for i in range(number_of_rules):
    field, b = lines[i].split(": ")
    matches = re.fullmatch("(\d+)-(\d+) or (\d+)-(\d+)", b)
    m = matches.groups()
    ranges = (int(m[0]), int(m[1]), int(m[2]), int(m[3]))
    rules[field] = lambda x, ranges=ranges: ranges[0] <= int(x) <= ranges[1] or ranges[2] <= int(x) <= ranges[3]

def error(value): # return 0 if the value satisfies at least one rule
    for rule in rules.values():
        a = 0 if rule(value) else value
        if a == 0:
            return a
    return value

error_rate = 0
for i in range (nearby_tickets, len(lines)):
    values = lines[i].split(',')
    error_rate += sum([error(int(value)) for value in values])
print(error_rate)

print('----------- Part 2 -----------')
def read_by_column(lines):
    by_row, by_column = [], [] # row and column matrices
    for i in range(nearby_tickets, len(lines)):
        cols = lines[i].split(',')
        if all([error(c) == 0 for c in cols]):
            by_row.append(cols)
    for colnum in range(len(by_row[0])):
        col = [int(row[colnum]) for row in by_row]
        by_column.append(col)
    return by_column

def find_compatible_fields(col):
    compatible_rules = set()
    for field, rule in rules.items():
        if all(map(lambda x: rule(x), col)):
            compatible_rules.add(field)
    return compatible_rules

def find_possible_matches(columns):
    possible_fields = {}
    for ncol, col in enumerate(columns):
        possible_fields[ncol] = find_compatible_fields(col)
    return possible_fields

identified_cols, identified_fields = set(), set()
mapping = {}
def identify(columns, possible_fields):
    for ncol in range(len(columns)):
        if ncol not in identified_cols: # if the column hasn't been identified
            if len(possible_fields[ncol]) == 1: # position found !
                found = list(possible_fields[ncol])[0]
                identified_cols.add(ncol)
                identified_fields.add(found)
                mapping[found] = ncol
            else:
                possible_fields[ncol] = possible_fields[ncol] - identified_fields
    return mapping, possible_fields

def answer(mapping):
    cols = lines[my_ticket].split(',')
    product = 1
    for field, col in mapping.items():
        if field.startswith('departure'):
            product *= int(cols[col])
    return product

columns = read_by_column(lines)
possible_matches = find_possible_matches(columns)
while(len(identified_cols) < len(columns)):
    mapping, possible_matches = identify(columns, possible_matches)
    #print(mapping)
print(answer(mapping))




