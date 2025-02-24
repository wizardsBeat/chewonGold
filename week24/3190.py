from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)] 

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 

L = int(input())
directions = []
for _ in range(L):
    X, C = input().split()
    directions.append((int(X), C)) 

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([(0, 0)]) 
direction = 0 
time = 0 
idx = 0 

while True:
    time += 1
    head_x, head_y = snake[-1] 
    nx = head_x + dx[direction]
    ny = head_y + dy[direction] 
    
    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 0
        snake.append((nx, ny))
    else:
        snake.append((nx, ny))
        snake.popleft()

    if idx < L and time == directions[idx][0]:
        if directions[idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        idx += 1

print(time)
