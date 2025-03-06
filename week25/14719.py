import sys

input = sys.stdin.readline

h, w = map(int,input().split())

block = list(map(int, input().split()))
answer = 0
for i in range(1,w-1):
    leftnum = max(block[:i])
    rightnum = max(block[i+1:])
    score = (min(leftnum, rightnum) - block[i])
    if score > 0:
        answer += score

print(answer)