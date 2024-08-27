import sys

# 문장 입력 받기
stream = sys.stdin.readline()

# 양쪽에 커서 두기
left_stack = list(stream) # 왼쪽 스택에는 stream을 list 형태로 담기
right_stack = [] # 빈 스택

# 명령어 처리
for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().split(' ')
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
print(''.join(left_stack + right_stack[::-1]))
        