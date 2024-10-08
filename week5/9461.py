# 백준 9461번 풀이

T = int(input())

for _ in range(T):
    n = int(input())

    if n < 4: # n이 4 미만일 경우에는 계산 불필요
        print(1)
    
    else:
        dp = [0] * (n + 1) # 필요한 만큼 dp 배열 생성
        dp[1], dp[2], dp[3] = 1, 1, 1 # 초기값 지정
        
        for i in range(4, n + 1): # 4에서부터 계산
            dp[i] = dp[i - 2] + dp[i - 3] # P(N) = P(N-2) + P(N-3)으로 계산됨

        print(dp[n])