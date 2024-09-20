import sys

input = sys.stdin.readline
poll = input().strip()
stack = []
num = 0
for i in range(len(poll)):
    if poll[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if poll[i-1] == "(":
            num += len(stack)
        else:
            num += 1

print(num)
