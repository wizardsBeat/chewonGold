def padovan_sequence(n):
    # 초기값 설정
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    
    # 점화식을 이용하여 수열을 계산
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    return dp[n]

T = int(input())
n = [] * T
for _ in range(T):
    n.append(int(input()))

for i in range(T):
    print(padovan_sequence(n[i]))
