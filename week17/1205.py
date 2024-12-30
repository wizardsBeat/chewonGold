import sys

input = sys.stdin.readline

n, s, p = map(int, input().split())

if n == 0:
    print(1)

else:
    rank = list(map(int, input().split()))

    i = 0
    while i < n and rank[i] > s:
        i += 1
    answer = i + 1


    if answer > p:
        print(-1)
    else:
        samescore = []
        for x in range(len(rank)):
            if rank[x] == s:
                samescore.append(x)

        if samescore and samescore[-1] + 1 >= p:
            print(-1)
        else:
            print(answer)