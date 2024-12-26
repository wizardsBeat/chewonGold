import sys

input = sys.stdin.readline

n = int(input().strip())
numlist = []

for _ in range(n):
    numlist.append(int(input().strip()))

numlist.sort()
answer = 0
for i in range(n):
    if numlist[i] != i+1:
        answer += abs((i+1) - numlist[i])
print(answer)
