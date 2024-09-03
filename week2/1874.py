# 수열의 개수 입력
import sys
n = int(sys.stdin.readline())

# 수열 리스트
li = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current_number = 1  # 현재 넣을 수 있는 숫자 (1부터 n까지)

for number in li:
    # 현재 숫자를 목표 수열의 숫자까지 push
    while current_number <= number:
        stack.append(current_number)
        result.append('+')
        current_number += 1
    
    # 스택의 최상단이 목표 숫자와 같으면 Pop
    if stack[-1] == number:
        stack.pop()
        result.append('-')
    # 목표수열을 만들 수 없을 때
    else:
        print("NO")
        break
else: # 수열을 정상적으로 다 만들었다면
    print('\n'.join(result))