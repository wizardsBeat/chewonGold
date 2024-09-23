import sys

sen = sys.stdin.readline().rstrip()
pstack = [] # 소괄호(parentheses) 스택
sstack = [] # 대괄호(square brackets) 스택


while sen != '.':
  for i in range (len(sen)):
    if sen[i] == '(':
      pstack.append(sen[i])
    elif sen[i] == '[':
      sstack.append(sen[i])
    elif sen[i] == ')':
      if pstack:
        pstack.pop()
    elif sen[i] == ']':
      if sstack:
        sstack.pop()
  if sstack or pstack:
    print('no')
  else:
    print('yes')
  sen = sys.stdin.readline().rstrip()