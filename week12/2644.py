n = int(input())

a, b = map(int, input().split())

m = int(input())
rellist = [[] for _ in range(n+1)]
visited =[False] * (n+1)

result = []
for i in range(m):
    x, y = map(int, input().split())
    rellist[x].append(y)
    rellist[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in rellist[v]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] -1)
