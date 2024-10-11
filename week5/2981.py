import sys
input = sys.stdin.readline

N = int(input().rstrip())    # 숫자의 개수
nums = [int(input().rstrip()) for _ in range(N)]

## 1. 주어진 수들 간의 차이를 구한다.
## 2. 그 차이들의 최대공약수를 구한다.
## 3. 최대공약수의 약수들을 구한다.

# 최대공약수
def GCD(a,b):
    while b:
        a, b = b, a%b
    return a

# 0번 숫자를 기준으로 다른 숫자들과의 차이를 구한다
# 0번 - 1번 차이를 1빠로 놓고..
result = abs(nums[1] - nums[0])

# 모든 다른 차이에 대해 최대공약수를 구한다
for i in range(2, N):
    result = GCD(result, abs(nums[i] - nums[0]))

# 약수 구하기
div = set()    # set을 써서 중복 제거 
for i in range(2, int(result**0.5)+1):
    if result % i == 0: 
        div.add(i)
        div.add(result // i)

div.add(result)
print(*sorted(div))