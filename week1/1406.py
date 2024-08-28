import sys
from collections import deque

input = sys.stdin.readline

#초기 문자열 입력
initial_string = list(input().strip())
#left stack에 deque형태로 초기 문자열 저장, 양쪽 방향에서 요소 추가 제거시 용이
left_stack = deque(initial_string)
right_stack = deque()

#입력할 명령어의 개수 입력해서 N에 저장
N = int(input().strip())

#N개만큼 for문 돌려볼게여
for i in range(N):
    #command 입력 받음
    command = input().strip()
    #L은 왼쪽으로 커서 이동이니까 커서를 기준으로  left_stack, right_stack으로 구분. 그래서 L을 하면 left_stack에 있던 것을 right_stack으로 옮기는 작업을 해줌
    if command == "L" and left_stack:
        right_stack.appendleft(left_stack.pop())
    #D는 오른쪽으로 커서 이동
    elif command == "D" and right_stack:
        left_stack.append(right_stack.popleft())
    #B는 커서 왼쪽 글자 삭제라 left_stack 맨 마지막거를 삭제해줌
    elif command == "B" and left_stack:
        left_stack.pop()
    #P는 커서 왼쪽에 추가니까 일단 입력문을 split먼저 해준 다음에 left_stack맨 뒤에 추가
    elif command.startswith("P "):
        i, char = command.split()
        left_stack.append(char)

#마지막으로 left_stack이랑 right_stack 합쳐주기
print(''.join(left_stack) + ''.join(right_stack))
