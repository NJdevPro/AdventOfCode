import timing
from collections import deque

lines =  open("puzzle18.txt","r").read().splitlines()

def eval(expr: str, precedence: dict) -> int:
    return evaluate(postfix_it(expr, precedence))

def evaluate(expr: str) -> int:
    stack = deque()
    for n, c in enumerate(expr):
        if c.isdigit():
            stack.append(int(c))
        elif c in ['+', '*']:
            a, b = int(stack.pop()), int(stack.pop())
            if c == '+':
                a += b
            elif c == '*':
                a *= b
            stack.append(a)
    return stack.pop()

def postfix_it(expr, preced: dict) -> str:
    stack = deque()
    postfix = ""
    for n, c in enumerate(expr):
        if c.isdigit():
            postfix += c
        elif c == '(':
           stack.append(c)
        elif c == ')':
           while stack and stack[-1] != '(':
              postfix += stack.pop()
           stack.pop()  # discard the left (
        elif c in ['+', '*']:
           if not stack or stack[-1] == '(':
              stack.append(c)
           else:
              while stack and stack[-1] != '('\
                      and preced[c] <= preced.get(stack[-1], 0):
                 postfix += stack.pop()
              stack.append(c)
    while stack:
        postfix += stack.pop()
    return postfix

[line.replace(' ', '') for line in lines]

precedence_normal = {'+':1, '*':2}
precedence1 = {'+':1, '*':1}
precedence2 = {'+':2, '*':1}
print(sum([eval(line, precedence1) for line in lines]))
print(sum([eval(line, precedence2) for line in lines]))
