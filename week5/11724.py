import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 설정
input = sys.stdin.readline


def dfs(node, graph, visited):
    # 현재 노드를 방문처리
    visited[node] = True

    # 현재 노드와 연결된 모든 노드를 재귀적으로 방문
    for neighbor in graph[node]:
        if not visited[neighbor]:   # 방문하지 않은 이웃 노드를 탐색
            dfs(neighbor, graph, visited)

# 입력받기
N, M = map(int, input().split())    # N: 정점의 개수, M: 간선의 개수
graph = [[] for _ in range(N + 1)]  # 인접 리스트로 그래프 초기화
visited = [False] * (N + 1)         # 방문 여부를 확인하는 리스트 (1~N 사용)

# 그래프 구성 (양방향 연결이므로 양쪽 모두 추가)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요수의 개수 카운트
cnt = 0

# 모든 노드를 확인하며 방문하지 않은 노드를 시작으로 DFS 실행
for node in range(1, N +1):
    if not visited[node]:   # 방문하지 않은 노드를 찾으면
        dfs(node, graph, visited)   # 해당 노드를 시작으로 DFS 탐색
        cnt += 1   # 새로운 연결 요소 발견

print(cnt)