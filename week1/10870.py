import sys

# input에 새 함수 정의
input = sys.stdin.readline
n = int(input())

# 피보나치 수열 함수
def fibo(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibo(m-1) + fibo(m-2)

# 계산
print(fibo(n))
