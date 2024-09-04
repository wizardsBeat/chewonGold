n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
answer = []

current = 1 # 1부터 시작

for num in seq:
    while current <= num: # 목표 숫자(num)에 도달할 때까지
        stack.append(current) # push
        answer.append('+')
        current += 1 # 다음 숫자

    if stack[-1] == num: # 스택의 최상단 숫자가 목표 숫자와 같으면
        stack.pop() # pop
        answer.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(answer))