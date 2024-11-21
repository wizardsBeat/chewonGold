N = int(input())

dp = [0] * (N+1)

for i in range(1,N+1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = (dp[i-1]+dp[i-2]) % 15746

print(dp[N])