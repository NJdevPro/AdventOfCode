
lines = open("puzzle3.txt","r").readlines()

print("-----------Part 1-----------")
length = 31
map = [[l[j] for j in range(len(l)-1)] for l in lines]

trees=0
step=[]
j=0
for i in range(323): # steps down
    j = j % length
    step.append((i,j,map[i][j]))
    if map[i][j] == '#':
        trees += 1
    j += 3 # steps to the right

print(step, sep='\n')
print("trees", trees)


print("-----------Part 2------------")
trees=0
step=[]
j=0
for i in range(0,323,2):
    j = j % length
    step.append((i,j,map[i][j]))
    if map[i][j] == '#':
        trees += 1
    j += 1

print(step, sep='\n')
print("trees", trees)

print(70*240*68*67*37)