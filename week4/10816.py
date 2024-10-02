import sys
input = sys.stdin.readline

n = int(input())
num_cards = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

plus = [0] * 10000001
minus = [0] * 10000001

for i in num_cards:
    if i >= 0: plus[i] += 1
    else: minus[i] += 1

for j in target:
    if j >= 0: print(plus[j], end=" ")
    else: print(minus[j], end=" ")