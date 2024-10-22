import sys
input = sys.stdin.readline

def BFS(x, y):
    #상하좌우
    dx = [-1, 1, 0,0]
    dy = [0,0,-1,1]
    queue = [(x,y)]
    baechu[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if baechu[nx][ny] == 1:
                #이 부분을 탐색할거라고 큐에 좌표를 추가
                queue.append((nx,ny))
                # 탐색했으니까 0으로 바꾸기(방문처리)
                baechu[nx][ny] = 0


T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    #배추밭 만들어줄게요... 일단 모든 땅은 0으로
    baechu = [[0]*(N) for _ in range(M)]
    
    count = 0
    for i in range(K):
        x, y = map(int, input().split())
        #배추 좌표 입력받아서 배추가 있으면 1로 변환
        baechu[x][y] = 1
    
    for a in range(M):
        for b in range(N):
            if baechu[a][b] == 1:
                BFS(a,b)
                count += 1
    
    print(count)



