import sys

# 양쪽에 커서 두기
left_stack = list(sys.stdin.readline().strip()) # 왼쪽 스택에는 list 형태로 담기
right_stack = [] # 빈 스택

# 명령어 처리
for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().strip().split(' ')
    if c[0] == 'L': # 커서를 왼쪽으로 한 칸
        if left_stack:
            right_stack.append(left_stack.pop())
    if c[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    if c[0] == 'B':
        if left_stack:
            left_stack.pop()
    if c[0] == 'P':
        left_stack.append(c[1])

# 결과 출력 (커서 왼쪽 + 오른쪽 스택의 역순)
left_stack.extend(reversed(right_stack))
print(''.join(left_stack))