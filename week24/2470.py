import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split(' ')))
min = 1000000000
min_list = [0,0]

for n in range(N):
    a = M[n]
    for m in range(N):
        if m == 0 or m == N:
            pass
        else:
            b = M[m]
            sum = a+b
            if sum < 0:
                sum *= -1
            if min > sum:
                min = sum
                min_list[0] = M[n]
                min_list[1] = M[m]
    
print(str(min_list[0])+" "+str(min_list[1]))


