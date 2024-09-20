inputs = input()
stack = []
total = 0

for i in range(len(inputs)):
    if inputs[i] == '(': # 쇠막대기 시작
        stack.append('(')
    else: # 쇠막대기 끝
        stack.pop()
        if inputs[i - 1] == '(':  # '()' = 레이저의 경우
            total += len(stack)  # 현재 스택에 있는 쇠막대기 수만큼 추가
        else: # 진짜 쇠막대기 끝
            total += 1  # 잘린 조각 1개 추가

print(total)