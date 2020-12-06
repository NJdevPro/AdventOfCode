lines = open("puzzle4.txt","r").readlines()

print("-----------Part 1-----------")
from collections import Counter
import itertools

records  = []
record = {}
for line in lines:
    if line in ['\n', '\r\n']:
        records.append(record)
        record = {}
    else:
        for entry in line.strip().split(' '):
            (key, value) = entry.split(':')
            record[key] = value
records.append(record)

invalid = list(itertools.filterfalse(lambda r: len(r) == 8 or (len(r) == 7 and not r.get('cid')), records))
print(len(records) - len(invalid))

print("-----------Part 2-----------")
import re

def is_valid(r) -> bool:
    if len(r) == 8 or (len(r) == 7 and not r.get('cid')):
        a = 1920 <= int(r['byr']) <= 2002
        b = 2010 <= int(r['iyr']) <= 2020
        c = 2020 <= int(r['eyr']) <= 2030
        height = r['hgt']
        d = (height.endswith('cm') and 150 <= int(height[:-2]) <= 193) or (height.endswith('in') and 59 <= int(height[:-2]) <= 76)
        e = re.fullmatch("#[0-9a-f]{6}", r['hcl'])
        f = r['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        g = re.fullmatch("\d{9}", r['pid'])
        return a and b and c and d and e and f and g
    return False

invalid = list(itertools.filterfalse(lambda r: is_valid(r), records))
print(len(records) - len(invalid))
