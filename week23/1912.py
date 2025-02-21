import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = []
hap = 0
for i in range (n):
  if arr[i] >= 0:
    hap += arr[i]
  else:
    if hap != 0:
      dp.append(hap)
      hap = 0
    dp.append(arr[i])

print(dp)