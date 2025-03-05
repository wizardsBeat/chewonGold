import sys

input = sys.stdin.readline

# 입력 받기
N = int(input())
M = list(map(int, input().split(' ')))

M.sort()

# 최대값 설정
min = float('inf')

# 0과 가장 가까운 조합 => return 값
min_list = [0,0]

# 투 포인터
lp, rp = 0, N-1

while(lp < rp):
    sum = M[lp] + M[rp]
    if abs(sum) < abs(min):
        min = sum
        min_list = [M[lp], M[rp]]
    
    if sum > 0:
        rp -= 1
    else:
        lp += 1
    
print(str(min_list[0])+" "+str(min_list[1]))


