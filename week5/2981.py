
import sys
import math

input = sys.stdin.readline
N = int(input().strip())
M = []

# 입력을 받는다
for i in range(N):
    M.append(int(input().strip()))

# 각 수의 차이를 구한다
diffs = []
for i in range(1, N):
    diffs.append(M[i] - M[i - 1])

# 차이들의 최대공약수를 구한다. Math의 gcd사용
g = diffs[0]
for i in range(1, len(diffs)):
    g = math.gcd(g, diffs[i])

# 최대공약수의 모든 약수를 구한다
answer = []
for i in range(2, int(g**0.5) + 1): # 제곱근을 사용하여 약수쌍을 찾으면 효율적임
    if g % i == 0:
        answer.append(i)
        if i != g // i:
            answer.append(g // i)
answer.append(g)

# 정렬 후 출력
answer.sort()
print(" ".join(map(str, answer)))
