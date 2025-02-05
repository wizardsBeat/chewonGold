import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
numbers = []
answer = []
for _ in range(n):
    num = int(input().strip())
    if num == 0:
        if len(numbers) != 0:
            answer.append(-(heapq.heappop(numbers)))
        else:
            answer.append(0)
    else:
        heapq.heappush(numbers, -num) #maxheap으로 만들어 주기 위해 앞에 부호 바꿔서 heappush해줬음

print('\n'.join(list(map(str, answer))))