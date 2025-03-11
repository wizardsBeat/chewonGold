import sys

input = sys.stdin.readline

origin = input().strip()
bomb = input().strip()
stack = []
bomblen = len(bomb)
for i in range(len(origin)):
    stack.append(origin[i])
    if ''.join(stack[-bomblen:]) == bomb:
        for _ in range(bomblen):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
        