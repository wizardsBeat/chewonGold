import sys

N, M = map(int, sys.stdin.readline().split())

sum = 0
cnt = 0
numbers = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    sum = 0
    for j in range(i,N):
        sum += numbers[j]
        if sum > M:
            break
        elif sum == M:
            cnt += 1
            break

print(cnt)
