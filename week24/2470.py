import sys
input = sys.stdin.readline

# 산성 용액 : 양수, 알칼리성 용액 : 음수

n = int(input())
cs = list(map(int, input().split())) # characteristic
cs.sort()
l = 0
r = n-1
tch = float('inf') # 두 용액의 합

while l < r:
  tmp = cs[l] + cs[r]
  if tmp == 0:
    ans = (cs[l], cs[r])
    break
  if abs(tmp) < tch:
    ans = (cs[l], cs[r])
    tch = abs(tmp)
  if abs(cs[l]) > abs(cs[r]):
    l += 1
  else:
    r -= 1

print(*ans)