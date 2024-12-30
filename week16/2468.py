import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
rain = [list(map(int, input().split())) for _ in range(n)]

def BFS(x,y, h, visited):
    dx = [-1, 1, 0,0]
    dy = [0,0,-1,1]
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<=ny < n and not visited[nx][ny] and rain[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx, ny))

maxcount = 0
maxh = max(max(row) for row in rain)

for h in range(maxh + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if rain[i][j] > h and not visited[i][j]:
                BFS(i, j, h, visited)
                count += 1
    
    maxcount = max(maxcount, count)

print(maxcount)