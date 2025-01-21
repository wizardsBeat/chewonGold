import sys
from collections import deque

input = sys.stdin.readline
answer = []

def BFS(x, y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque([(x, y)])
    island[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                queue.append((nx, ny))
                island[nx][ny] = 0

while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    island = []
    for _ in range(h):
        island.append(list(map(int, input().split())))

    num = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                BFS(i, j)
                num += 1
    answer.append(num)

print('\n'.join(map(str, answer)))
