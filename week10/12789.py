import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
slist = list(map(int, input().split()))

leftstack = deque()
rightstack = deque(slist)

possible = True
num = 1
while rightstack or leftstack:
    if rightstack and rightstack[0] == num:
        rightstack.popleft()
        num += 1
    elif leftstack and leftstack[-1] == num:
        leftstack.pop()
        num+=1
    elif rightstack:
        leftstack.append(rightstack.popleft())
    else:
        break


if leftstack:
    print("Sad")
else:
    print("Nice")