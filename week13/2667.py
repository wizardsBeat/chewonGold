import sys
#bfs로 푸는 방법
input = sys.stdin.readline
N = int(input().strip())

aptmap = [list(map(int, list(input().strip()))) for _ in range(N)]

answer = []
def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(x, y)]
    aptmap[x][y] = 0
    tmp = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or  ny >= N:
                continue
            if aptmap[nx][ny] == 1:
                tmp += 1
                queue.append((nx,ny))
                aptmap[nx][ny] = 0
    answer.append(tmp)
    
count = 0
for i in range(N):
    for j in range(N):
        if aptmap[i][j] == 1:
            bfs(i, j)
            count += 1
print(count)
print('\n'.join(map(str, sorted(answer))))