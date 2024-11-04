import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    nums = list(map(int, input().split()))
    answer = 0
    maxdigit = 0
    for i in range(N-1 ,-1, -1):
        if nums[i] < maxdigit:
            answer += maxdigit - nums[i]
        else:
            maxdigit = nums[i]
    
    print(answer)