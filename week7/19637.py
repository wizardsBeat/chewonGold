import sys
input = sys.stdin.readline

N, M = map(int, input().split())
character = []
for i in range(N):
    name, power = input().split()
    character.append([name, int(power)]) 

nums = []

for i in range(M):
    nums.append(int(input().strip())) 
    
for num in nums:
    right = len(character) - 1 
    left = 0
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if character[mid][1] >= num:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(character[answer][0])
