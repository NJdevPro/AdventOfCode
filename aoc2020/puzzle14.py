import itertools as it
import timing

lines =  open("puzzle14.txt","r").read().replace(' ','').splitlines()

print('----------- Part 1 -----------')
BITLEN = 36
def masking(val:str, mask:str):
    binary = bin(int(val))[2:]
    binary = list('0'*(BITLEN-len(binary)) + binary)
    mask = list(mask)
    for i in range(BITLEN):
        if mask[i] != 'X':
            binary[i] = mask[i]
    return int(str(''.join(binary)), 2)

mem = {}
mask = ''
for line in lines:
    left, right = line.split('=')
    if left.startswith('mem'):
        key = left.split('[')[1].replace(']', '')
        mem[key] = masking(right, mask)
    elif left.startswith('mask'):
        mask = right
print(sum(mem.values()))

print('----------- Part 2 -----------')

def masking2(val:str, initial_mask: str, mask:str):
    binary = bin(int(val))[2:]
    binary = '0'*(BITLEN-len(binary)) + binary
    masked = list(binary)
    for i in range(BITLEN):
        if initial_mask[i] in ('X', '1'):
            masked[i] = mask[i]
    return ''.join(masked)

def list_masks(addr):
    if addr.find('X') < 0:
        yield addr
    else:
        yield from list_masks(addr.replace('X','0',1))
        yield from list_masks(addr.replace('X','1',1))

mem = {}
for line in lines:
    left, right = line.split('=')
    if left.startswith('mem'):
        addr = left.split('[')[1].replace(']', '')
        masked = masking2(addr, xmask, xmask)
        masks = list(list_masks(xmask))
        for m in masks:
            mem[masking2(addr, xmask, m)] = int(right)
    elif left.startswith('mask'):
        xmask = right
print(sum(mem.values()))


