n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

def bfs(num):
    global k
    queue = []
    queue.append(num)
    while queue:
        tmp = queue.pop(0)
        if tmp == k:
            return visited[tmp]
        
        if tmp-1 >= 0 and visited[tmp-1] == 0:
            visited[tmp-1] = visited[tmp] + 1
            queue.append(tmp-1)

        if tmp+1 <= 100000 and visited[tmp+1] == 0:
            visited[tmp+1] = visited[tmp] + 1
            queue.append(tmp+1)

        if tmp*2 <= 100000 and visited[tmp*2] == 0:
            visited[tmp*2] = visited[tmp] + 1
            queue.append(tmp*2)
        
    return -1


print(bfs(n))