#### Password policies

lines = open("puzzle2.txt","r").readlines()

print("-----------Part 1------------")

def parse_line(line):
    policy, passwd = line.split(':')
    minmax, letter = policy.split(' ')
    mini, maxi = minmax.split('-')
    return (int(mini), int(maxi), letter.strip(), passwd.strip())

records = [parse_line(line) for line in lines]
print(records[1:5])

good, bad = [], []
for r in records:
    (mini, maxi, letter, passwd) = r
    if mini <= passwd.count(letter) <= maxi:
        good.append(r)
    else:
        bad.append(r)
print("good=", len(good))
print("bad=", len(bad))
#print(good)
#print(bad)

print("-----------Part 2------------")
good, bad = [], []
for r in records:
    (pos1, pos2, letter, passwd) = r
    l1_ok = passwd[pos1-1] == letter
    l2_ok = passwd[pos2-1] == letter
    if l1_ok != l2_ok:
        good.append(r)
    else:
        bad.append(r)
print("good=", len(good))
print("bad=", len(bad))
print(good)
print(bad)
