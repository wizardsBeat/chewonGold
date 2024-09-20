# 정점의 개수(N), 간선의 개수(M), 정점의 번호(V)
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

# 간선이 연결하는 두 정점의 번호 입력 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호가 작은 것부터 방문하기 위해 정렬
for edges in graph:
    edges.sort()

# DFS
def dfs(v, visited):
    visited[v] = True # 방문한 정점 = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]: # 방문 안한 정점만
            dfs(neighbor, visited)

# BFS
from collections import deque

def bfs(v):
    visited = [False] * (N + 1)
    queue = deque([v]) # 시작 정점을 큐에 추가
    visited[v] = True # 방문한 정점 = True
    while queue: # 큐에 탐색할 노드가 있는 동안
        node = queue.popleft() # 큐 왼쪽 끝에서 노드 꺼내기
        print(node, end=' ')
        for neighbor in graph[node]: # 현재 노드와 연결된 노드들
            if not visited[neighbor]: # 방문 안한 노드만
                queue.append(neighbor) # 큐에 추가 
                visited[neighbor] = True # 연결된 노드를 방문 처리

# DFS 실행
visited = [False] * (N + 1)
dfs(V, visited)
print()

# BFS 실행
bfs(V)
print()