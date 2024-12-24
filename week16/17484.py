import sys

input = sys.stdin.readline

n, m = map(int, input().split())
spacemap = []
direction = [-1, 0, 1]


for _ in range(n):
    spacemap.append(list(map(int, input().split())))

def dfs(col, row, d, low, answer):
    if col == n-1:
        return min(low, answer)
    for i in direction:
        if i != d:
            if 0<=col<n and 0<= row + i < m:
                low = dfs(col+1, row+i, i, low, answer + spacemap[col+1][row+i])
    
    return low

low = int(sys.maxsize)
for i in range(m):
    low = min(dfs(0, i, 2, low, spacemap[0][i]), low)

print(low)

