from sys import stdin

# 초기 문자열 입력 받기
li = list(input())
N = int(input())


# 커서 위치
left = li # 초기에는 모든 문자가 커서 왼쪽에 있음을 가정
right = []


for _ in range(N):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

# 결과 출력
print(''.join(left + right[::-1]))
