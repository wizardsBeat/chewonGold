from collections import deque
import sys

input = sys.stdin.readline

N = int(input()) # 탑의 개수
heights = list(map(int, input().split())) # 각 탑의 높이

stack = []  # 스택에 (탑의 인덱스, 탑의 높이)를 저장
result = [0] * N # 각 탑의 레이저 신호를 수신하는 탑의 번호를 저장
for i in range(N):
    current_height = heights[i]

    # 현재 탑보다 낮거나 같은 탑을 스택에서 제거
    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    if stack:
        # 스택의 최상단에 있는 탑이 현재 탑의 레이저 신호를 수신
        result[i] = stack[-1][0] + 1 # 인덱스는 1부터 시작하므로 +1
    else:
        # 스택이 비어있다면 레이저 신호를 수신하는 탑이 없음
        result[i] = 0

    stack.append((i, current_height))

print(' '.join(map(str, result)))