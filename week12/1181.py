import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
arrlist  = [[] for _ in range(51)] 
for _ in range(n):
    tmp = input().strip()
    arrlist[len(tmp)].append(tmp)

answer = []
for i in range(51):
    if len(arrlist[i])>0:
        arrlist[i] = sorted(list(set(arrlist[i])))
        answer += arrlist[i]


print('\n'.join(answer))