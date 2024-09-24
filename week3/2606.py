def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

num = int(input())  # 컴퓨터의 수
connect = int(input())  # 연결 수

graph = [[] for _ in range(num + 1)] # 컴퓨터들간의 연결을 이차원 배열에 저장.

for _ in range(connect): # ex 1,2번 컴퓨터가 연결되어 있다면 1번과 2번 모두 서로의 번호 저장
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)

visited = [False] * (num + 1)

dfs(graph, 1, visited)

print(visited.count(True) - 1)
