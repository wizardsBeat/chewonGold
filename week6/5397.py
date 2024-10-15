#1406번이랑 비슷하게 풀었어요
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
L = []

answer = []  
for i in range(N):
    L.append(list(input().strip())) # 입력 먼저 받고 L list에 append
    # 커서를 기준으로 left_stack, right_stack 일단 둘 다 비워놓을 것임
    left_stack = deque()
    right_stack = deque()
    for j in range(len(L[i])):
        if L[i][j] == "<" and left_stack:
            right_stack.appendleft(left_stack.pop())
        elif L[i][j] == ">" and right_stack:
            left_stack.append(right_stack.popleft()) # popleft 하려고 deque 사용
        elif L[i][j] == "-" and left_stack:
            left_stack.pop()
        elif L[i][j].isalpha() or L[i][j].isnumeric(): # 알파벳이나 숫자면 left_stack에 append
            left_stack.append(L[i][j])
    answer.append("".join(left_stack+right_stack))


print("\n".join(answer))
