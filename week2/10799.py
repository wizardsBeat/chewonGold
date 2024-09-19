q = input()
stack = []
answer = 0

for idx in range(len(q)):
    if q[idx] == '(': # 열린 괄호는 추가
        stack.append('(')
    else: # 닫는 괄호는 삭제
        stack.pop()
        if q[idx-1] == '(': # 레이저인 경우
            answer += len(stack)
        else: answer += 1 # 막대의 끝인 경우

print(answer)