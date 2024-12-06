import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
numlist = []
answer = []
for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if numlist:
            answer.append(heapq.heappop(numlist))
        else:
            answer.append(0)
    else:
        heapq.heappush(numlist, x)

print('\n'.join(map(str, answer)))