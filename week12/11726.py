N = int(input())

i=0
dp = [0] * 1001
for i in range(N+1):
    if i <= 3:
        dp[i] = i
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[N])
