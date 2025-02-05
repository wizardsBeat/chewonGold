import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    score = [0] * (N + 1)
    for i in range(N):
        d, i = map(int, input().split())
        score[d] = i
    
    answer = 1
    scoremax = score[1]
    for i in range(2, N+1):
        if score[i] < scoremax:
            scoremax = score[i]
            answer += 1

    print(answer)
