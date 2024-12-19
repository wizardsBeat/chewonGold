import sys

input = sys.stdin.readline

n, m = map(int, input().split())

keyword =  set(input().strip() for _ in range(n))

for _ in range(m):
    search = set(input().strip().split(','))
    keyword -= search
    print(len(keyword))

