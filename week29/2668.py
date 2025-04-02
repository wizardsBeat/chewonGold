import sys
sys.setrecursionlimit(10000)

def dfs(start, current, visited, path, graph, result):
    if visited[current]:
        if current in path:  # 사이클 형성 확인
            result.update(path[path.index(current):])
        return
    
    visited[current] = True
    path.append(current)
    dfs(start, graph[current], visited, path, graph, result)
    path.pop()

n = int(sys.stdin.readline().strip())
graph = {i: int(sys.stdin.readline().strip()) for i in range(1, n + 1)}

result = set()

for i in range(1, n + 1):
    if i not in result:
        visited = {j: False for j in range(1, n + 1)}
        dfs(i, i, visited, [], graph, result)

print(len(result))
for num in sorted(result):
    print(num)
