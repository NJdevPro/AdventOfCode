numbers = [int(n) for n in open("puzzle9.txt", 'r').read().splitlines()]

print('----------- Part 1 -----------')
def find_sum(n):
    for n1 in range(n-25,n):
        for n2 in range(n-25,n):
            if n1 == n2:
                continue
            if numbers[n1] + numbers[n2] == numbers[n]:
                return n+1, numbers[n]
    print(n+1, numbers[n])
    return n+1, numbers[n]

for n in range(25, len(numbers)):
    idx, ss = find_sum(n)

print('----------- Part 2 -----------')

def find_sum2(sum1, n):
    #print(sum1, n)
    for n1 in range(n):
        for n2 in range(n1+1,n,1):
            s = sum(numbers[n1:n2])
            if s > sum1:
                break
            if s == sum1:
                print(s, n1+1, n2+1, min(numbers[n1:n2])+max(numbers[n1:n2]), numbers[n1:n2])

find_sum2(85848519, 554)
