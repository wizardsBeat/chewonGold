import sys
sys.setrecursionlimit(10000)    # 재귀 깊이 한도를 10000으로 늘리기
input = sys.stdin.readline

# 정점 개수, 간선 개수
N, M = map(int, input().rstrip().split())

# 정점 개수만큼 빈 리스트 만들기 -> 연결된 정점 저장할
graph = [[] for _ in range(N)]

# 각 점에 어느 점이 연결 됐는지...
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    
    # 양방향이므로 양쪽에 추가해주기
    # index를 위해 -1 해준다
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

# 방문 여부
visited = [False] * N

def dfs(v): # v = 현재 방문하는 정점
    visited[v] = True    # 현재 정점 = 방문 처리
    for neighbor in graph[v]:    # 이 점에 연결된 점들 탐색
        if not visited[neighbor]:    # 연결된 점 중에 방문 안한 점이 있으면
            dfs(neighbor)    # 그 점에 대해 다시 dfs

result = 0

for i in range(N):
    if not visited[i]:    # 아직 방문하지 않은 점이 있으면
        dfs(i)    # 그 정점에서 dfs 시작
        result += 1 # 새 연결 요소가 발견됐으므로 개수 증가

print(result)