import sys

input = sys.stdin.readline

n = int(input().strip())

numbers = list(map(int, input().split()))
dp = [0] * len(numbers)
dp[0] = numbers[0]

for i in range(len(numbers)):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

print(max(dp))

