N = int(input())

M = []

for i in range(N):
    num = list(map(int, input().split()))
    
    for n in num:
        if len(M) < N:
            M.append(n)
            M.sort()
        else:
            if M[0] < n:
                M[0] = N
                M.sort()

print(M[0])