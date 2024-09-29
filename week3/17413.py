import sys
from collections import deque
S = sys.stdin.readline().strip() + " "
stack = deque()
result = "" 
notreverse = False #특수문자 안에 있는지 아닌지 확인하기 위한 bool 변수

for s in S:
    if not notreverse:
        if s ==" ": # 공백 일때
            while stack: # 지금까지 저장한 stack 반복문 돌려서 맨 뒤 원소부터 result에 더해주기
                result += stack.pop()
            result += " "
        
        else:
            if s =="<": # 괄호 만났을 때도 지금까지 저장한 stack 반복문 돌려서 result에 뒤원소부터 넣어줌
                while stack:
                    result += stack.pop() 
                notreverse = True # 특수문자 안에 있기 때문에 true로 바꿔줌
            stack.append(s) 
        
    else:
        stack.append(s)
        if s == ">": # 닫는 괄호 만났을 때는 deque니까 popleft 사용해서 뒤집지 않고 저장해주기
            while stack:
                result += stack.popleft()
            notreverse = False

print(result)