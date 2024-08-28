import sys
input = sys.stdin.readline

left = list(input().rstrip()) # 커서 왼쪽 문자들
right = [] # 커서 오른쪽 문자들 (처음엔 빈 상태)

m = int(input())
for _ in range(m):
    command = input().rstrip()

    # 커서 왼쪽 이동
    if command[0] == 'L':
        if left:
            right.append(left.pop()) # 왼쪽 스택에서 오른쪽 스택으로 이동
    # 커서 오른쪽 이동
    elif command[0] == 'D':
        if right:
            left.append(right.pop()) # 오른쪽 스택에서 왼쪽 스택으로 이동
    # 커서 왼쪽 문자 삭제
    elif command[0] == 'B':
        if left:
            left.pop() # 왼쪽 스택에서 맨 마지막 문자 삭제
    # 커서 왼쪽 문자 추가
    elif command[0] == 'P':
        left.append(command.split()[1]) # 왼쪽 스택의 맨 마지막에 문자 추가

print(''.join(left + right[::-1])) # 왼쪽 + 오른쪽(역순)