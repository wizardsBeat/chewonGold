import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))

cnt = 0

nums.sort()
s = 0
e = n-1

while s < e: # 왼쪽 포인터가 오른쪽 포인터보다 왼쪽에 있어야 함
  if nums[e] + nums[s] < m: # 합이 m보다 작으면 작은 쪽을 키워줘야 함
    s += 1
  
  elif nums[e] + nums[s] > m: # 합이 m보다 크면 큰 쪽을 줄여줘야 함
    e -= 1
  
  else:
    cnt += 1
    s += 1
    e -= 1

print(cnt)