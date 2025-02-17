import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input().strip())
c = list(map(int, input().split()))
zero = deque()
for i in range(n):
    if a[i] == 0:
        zero.append(b[i])

for number in c:
    if zero:
        tmp = zero.pop()
        zero.appendleft(number)
        print(tmp, end=' ')
    else:
        print(number , end=' ')
