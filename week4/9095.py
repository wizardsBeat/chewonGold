# 백준 9095번 풀이

T = int(input()) # 테스트 케이스 개수 입력

for _ in range(T):
    n = int(input()) # 각각의 테스트 케이스 입력

    dp = [0] * (n + 1) # n까지의 합 저장할 배열 생성 (초기값 0)
    dp[0] = 1 # 0을 만드는 방법 1가지

    # 1부터 n까지 i에 대해 dp 값을 계산
    for i in range(1, n + 1):
        if i >= 1: # (i - 1)에서 1 더한 경우
             dp[i] += dp[i - 1]
        if i >= 2: # (i - 2)에서 2 더한 경우
             dp[i] += dp[i - 2]
        if i >= 3: # (i - 3)에서 3 더한 경우
             dp[i] += dp[i - 3]

    print(dp[n]) # 전체 개수 출력
    