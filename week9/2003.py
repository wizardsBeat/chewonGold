N, M = map(int, input().split())

A = list(map(int, input().split()))

answer = 0
num = 0
end = 0
#포인터 시작점을 for 문으로 돌리는 i가 됨
for i in range(N):
    while num < M and end < N: #포인터 끝점이 end
        num += A[end]
        end+= 1
    if num == M:
        answer += 1
    num -= A[i]

print(answer)