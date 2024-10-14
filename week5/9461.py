import sys
input = sys.stdin.readline

P = [0, 1, 1, 1]
n = 4
while True:
    if n > 100: break
    P.append(P[n-2] + P[n-3])
    n+=1

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    print(P[N])