import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
pn = 1 # problem number

while n != 0:
  cave = [list(map(int, input().split())) for _ in range (n)] # 도둑루피의 크기
  dp = [[0]*n for _ in range (n)]
  visited = [[False]*n for _ in range (n)] # 방문 리스트
  
  nv = deque([(0, 0)])
  dp[0][0] = cave[0][0]

  while nv:
    x, y = nv.popleft()
    visited[x][y] = True
    
    for dx, dy in directions:
      nx, ny = x+dx, y+dy

      if 0 <= nx < n and 0 <= ny < n:
        if visited[nx][ny]: # 이미 값이 존재
          if dp[nx][ny] > dp[x][y] + cave[nx][ny]:
            nv.append((nx, ny)) # 최소값이 갱신되었다면 다시 탐색해야 함
            dp[nx][ny] = dp[x][y] + cave[nx][ny]
        else:
          dp[nx][ny] = dp[x][y] + cave[nx][ny]
          nv.append((nx, ny))
          visited[nx][ny] = True

  print('Problem %d: %d'%(pn, dp[n-1][n-1]))
  n = int(input())
  pn += 1