import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
nodes = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def bfs(start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in nodes[current]:
            if parents[neighbor] == 0:
                parents[neighbor] = current
                queue.append(neighbor)

bfs(1)

print('\n'.join(map(str, parents[2:])))
