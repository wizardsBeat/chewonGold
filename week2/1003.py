# 테스트 케이스 입력받기
T = int(input())

# 0과 1을 담을 수 있는 리스트 정의
max_n = 40  # 문제에서 주어진 n의 최대값
dp = [[0, 0] for _ in range(max_n + 1)]

# 초기값 설정
dp[0] = [1, 0]  # fibo(0)은 0이 1번, 1이 0번 호출됨
dp[1] = [0, 1]  # fibo(1)은 0이 0번, 1이 1번 호출됨

# 동적 프로그래밍으로 0과 1의 호출 횟수 계산
for i in range(2, max_n + 1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0의 호출 횟수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1의 호출 횟수

# 각 테스트 케이스에 대해 결과 출력
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])