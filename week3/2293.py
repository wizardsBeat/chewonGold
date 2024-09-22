# 백준 2293번 문제 풀이

n, k = map(int, input().split()) # 동전 가짓수 및 목표 금액 입력

# 각 동전 가치 입력
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[i]: i원을 만드는 방법의 수
dp = [0] * (k + 1)  # dp는 모두 0부터 시작
dp[0] = 1  # 0원 만드는 방법 1가지 저장

for coin in coins:
    # 목표 금액(dp[k])까지 각 동전의 가치로 만들 수 있는 방법 수 누적
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k]) # 목표 금액 만드는 가짓수 출력