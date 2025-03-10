import sys
from collections import deque
input = sys.stdin.readline
problems = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(cave, n):
    number = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    number[0][0] = cave[0][0]
    
    while queue:
        x, y = queue.popleft()
        coin = number[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                tmp = coin + cave[nx][ny]
                
                if tmp < number[nx][ny]:
                    number[nx][ny] = tmp
                    queue.append((nx, ny))
    
    problems.append(number[-1][-1])
    
while True:
    n = int(input().strip())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    bfs(cave, n)

for i in range(len(problems)):
    print("Problem " + str(i + 1) + ": " + str(problems[i]))