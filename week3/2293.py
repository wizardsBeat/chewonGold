n, k = map(int, input().split())

money = []
dp = [0] * (k +1)
dp[0] = 1

for _ in range(n):
    a = int(input())
    money.append(a)

for m in money:
    for i in range(m, k+1):
        dp[i] += dp[i-m]

print(dp[k])