import sys

# dfs (깊이우선탐색) 함수
def dfs(idx):
    global visited 
    visited[idx] = True # 방문했으니 True
    print(idx, end=' ') # 방문한 곳은 출력
    for next in range(1, N+1):
        if graph[idx][next] and not visited[next]: # 방문할 곳이 존재하고 그게 방문했던 곳이 아닐 시
            dfs(next)
    

# bfs (넓이우선탐색) 함수
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if graph[cur][next] and not visited[next]:
                visited[next] = True
                q.append(next)

input = sys.stdin.readline

# N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# graph 초기화
graph = [[False] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)

# graph 정보 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = True
    graph[B][A] = True
    
# dfs 시작
dfs(V)
print()
    

# bfs 시작
visited = [False] * (N+1) # 다시 초기화
q = [V] # 시작할 정점을 넣기
visited[V] = True
bfs()


