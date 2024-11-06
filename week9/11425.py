import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = set()

for _ in range(N):
    S.add(input().strip())

answer = 0
for _ in range(M):
    tmp = input().strip()
    if tmp in S:
        answer += 1

print(answer)
