import sys

input = sys.stdin.readline

n = int(input().strip())
meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append([start, end])


meeting.sort(key=lambda x: (x[1], x[0])) #끝나는 시간 기준으로 정렬, 끝나는 시간이 같다면 시작하는 시간이 빠른거 먼저 정렬해주기

answer = 0
tmp = 0
for i in range(n):
    if (tmp <= meeting[i][0]):
        tmp = meeting[i][1]
        answer += 1


print(answer)