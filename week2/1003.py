import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 개수

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

for _ in range(T):
  N = int(sys.stdin.readline()) # 테스트 케이스
  if N == 0:
    print ("1 0")
  elif N == 1:
    print ("0 1")
  else:
    print(fibo(N-1), fibo(N))