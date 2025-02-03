import sys

input = sys.stdin.readline

n = int(input().strip())

graph = [list(input().strip()) for _ in range(n)]

friends = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if k == j: #자기자신
                continue
            if graph[j][k] == 'Y' or (graph[j][i] == 'Y' and graph[i][k] == 'Y'): #이미 친구인 경우 or 2-친구인 경우
                friends[j][k] = 1

answer = 0

for row in friends:
    answer = max(answer, sum(row))

print(answer)
