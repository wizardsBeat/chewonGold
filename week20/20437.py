import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    w = input().strip()
    k = int(input().strip())
    
    alp = defaultdict(list)
    for i, char in enumerate(w):
        alp[char].append(i)
    
    result = []
    for indices in alp.values():
        if len(indices) >= k:
            for i in range(len(indices) - k + 1):
                result.append(indices[i + k - 1] - indices[i] + 1)
    
    if result:
        print(min(result), max(result))
    else:
        print(-1)
