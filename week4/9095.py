import sys

input = sys.stdin.readline

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 배열
test = []

# 테스트 케이스 입력 받기
for _ in range(T):
    test.append(int(input()))

# 가장 큰 n 값을 찾기 (최대 n까지 dp 테이블을 미리 계산하기 위함)
max_n = max(test)

# 다이나믹 프로그래밍 테이블 초기화
dp = [0] * (max_n + 1)

# 초기 값 설정 (기본 경우의 수)
dp[0] = 1  # 0을 만드는 방법은 아무것도 더하지 않는 1가지 방법
if max_n >= 1:
    dp[1] = 1  # 1을 만드는 방법은 1을 더하는 1가지 방법
if max_n >= 2:
    dp[2] = 2  # 2를 만드는 방법은 (1+1), (2)로 2가지 방법
if max_n >= 3:
    dp[3] = 4  # 3을 만드는 방법은 (1+1+1), (1+2), (2+1), (3)로 4가지 방법

# 다이나믹 프로그래밍으로 dp 테이블 채우기
for i in range(4, max_n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 각 테스트 케이스에 대해 결과 출력
for n in test:
    print(dp[n])