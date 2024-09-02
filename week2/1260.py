from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())


# 정점과 간선을 표현한 2차원 배열 그래프
graph = [[False] * (N+1) for _ in range(N+1)]
# 방문했다는 내용
visited = [False] * (N+1)


# 1. graph 정보 입력
for _ in range(M): # M개의 간선이 존재함
    a, b = map(int, input().split())
    # ab 양방향 갈 수 있다는 것을 명시
    graph[a][b] = True
    graph[b][a] = True



# dfs 함수 정의
def dfs(idx):
    # 나 도착했소
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, N+1):
        # 방문한적이 없거나 해당 인덱스에서 다음 위치로 갈 수 있다면
        if not visited[next] and graph[idx][next]:
            dfs(next)

# bfs 함수 정의
def bfs(V):
    q = deque([V])
    visited[V] = True # 방문처리
    # q가 빌때까지 돌기
    while q:
        V = q.popleft() # q에 있는 첫번째값 꺼냄
        print(V, end=" ")
        for next in range(1, N+1):
            if not visited[next] and graph[V][next]: # 해당 위치를 방문하지 않았고 V와 연결되어 있다면
                q.append(next)
                visited[next] = True


# 2. dfs
dfs(V)
print()

# 3. bfs
# 초기화
visited = [False] * (N+1)
bfs(V)