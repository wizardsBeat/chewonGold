N = int(input())
heights = list(map(int, input().split()))
# heights = [6, 9, 5, 7, 4]

stack = []    # (idx, height)
result = [0] * N

for i in range(N):
    # 현재 탑보다 낮은 탑들은 스택에서 제거하기
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()

    # 스택에 있는 탑이 현재 탑보다 크면 그 인덱스를 result에 저장
    if stack:
        result[i] = stack[-1][0] + 1
    
    # 현재 탑을 스택에 추가 (idx, height)
    stack.append((i, heights[i]))

print(" ".join(map(str, result)))