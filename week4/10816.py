import sys

input = sys.stdin.readline

num = int(input().strip())
nums = list(map(int, input().split()))

numdict = dict() # dictionary에 숫자로 key, 개수를 value로 저장할거임 {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1} 이런식으로

for i in nums:
    numdict[i] = numdict.get(i, 0) + 1 # 키가 만약 없으면 0으로 초기화 해준 뒤 +1 해줌
searchnum = int(input().strip())
searchnums = list(map(int, input().split()))

answer = []
for i in searchnums:
    answer.append(numdict.get(i,0)) # 키가 없으면 0으로 표시


print(' '.join(list(map(str, answer)))) # str로 맵핑해준 뒤 join해서 str로 print