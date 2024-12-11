import sys

input = sys.stdin.readline

n = int(input().strip())

arr = [ int(input().strip()) for _ in range (n)]
dp = [0 for _ in range(n)] 
dp[0] = arr[0]

for i in range(1, n):
    if i == 1:
        dp[i] = max(arr[0]+arr[1], arr[1])
    elif i == 2:
        dp[2] = max(arr[0] + arr[2], arr[1]+arr[2])
    else:
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])


print(dp[-1])
