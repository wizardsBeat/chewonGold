# 백준 4949번 문제 풀이

while True:
    str = input()
    stack = []

    if str == '.': # 마지막에 온점 입력받을 경우 끝냄
        break

    for i in str: # 문자열 돌며 여는 괄호 있을 경우 스택에 추가
        if i == '(' or i == '[': 
            stack.append(i)

        elif i == ')': # 닫힌 괄호 올 경우, 스택에 여는 괄호가 이미 있다면 제거
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else: # 스택이 비어 있을 경우 닫힌 괄호 추가
                stack.append(i)
                break

        elif i == ']': 
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if len(stack) == 0: # 스택이 비어 있을 경우 균형이 맞음
        print('yes')

    else: # 스택 비어 있지 않을 경우 균형 맞지 않음
        print('no')
