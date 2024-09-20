
# 지금까지 얻은 레이저의 개수
# (이 등장하고 ) 나올때까지 레이저의 개수 + 1을 하면 잘라진 개수

import sys

li = sys.stdin.readline().rstrip()

def solution(s):
    stack = []
    pieces = 0  # 잘려진 조각 수

    for i in range(len(s)):
        if s[i] == '(':  # 여는 괄호는 스택에 추가 (쇠막대기의 시작)
            stack.append('(')
        else:  # 닫는 괄호인 경우
            stack.pop()  # 일단 스택에서 하나 제거 (쇠막대기 끝 or 레이저)
            if s[i - 1] == '(':  # 바로 이전이 여는 괄호이면 레이저
                pieces += len(stack)  # 스택에 있는 쇠막대기 수만큼 조각이 생김
            else:  # 쇠막대기의 끝을 만난 경우
                pieces += 1  # 쇠막대기 하나가 끝났으므로 조각 하나 추가

    return pieces


print(solution(li))