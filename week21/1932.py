import sys

n = int(input().strip())
numarr = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    numarr.append(list(map(int, input().split())))

dp[0][0] = numarr[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + numarr[i][j] # 제일 왼쪽 원소 바로 위쪽에서 가져옴
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + numarr[i][j] # 제일 오른쪽 원소, 왼쪽 위에서 가져옴
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + numarr[i][j]  # 왼쪽, 오른쪽 비교해서 큰 값을 가져옴

print(dp)
print(max(max(dp)))