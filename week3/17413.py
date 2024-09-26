import sys

sen = sys.stdin.readline().strip()
arrow = False
stack = []
answer = []

for s in sen:
  if s == '<':
    if stack: # 괄호가 열렸는데 stack이 있다면 지금까지 나왔던 문장을 거꾸로 출력
      stack.reverse()
      answer.extend(stack)
      stack = []
    arrow = True # 괄호 열림
    answer.append(s)
  elif s == '>':
    arrow = False # 괄호 닫힘
    answer.append(s)
  elif s == ' ':
    if arrow == False: # 괄호 바깥에 띄어쓰기가 있다면 지금까지 나왔던 문장을 거꾸로 출력
      stack.reverse()
      answer.extend(stack)
      stack = []
    answer.append(s) # 괄호 안의 띄어쓰기는 순서대로 출력
  elif arrow == True: # 괄호 안의 모든 문장은 순서대로 출력
    answer.append(s)
  else:
    stack.append(s)

stack.reverse()
answer.extend(stack) # 마지막 부분 처리

print(''.join(answer)) # answer의 모든 항목을 띄어쓰기 없이 출력