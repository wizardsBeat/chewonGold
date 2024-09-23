import sys

sen = sys.stdin.readline().rstrip()

while sen != '.':
  stack = []
  for i in range (len(sen)):
    if sen[i] == '(':
      stack.append(sen[i])
    elif sen[i] == '[':
      stack.append(sen[i])
    elif sen[i] == ')':
      if stack:
        if stack[-1] == '(':
          stack.pop()
    elif sen[i] == ']':
      if stack:
        if stack[-1] == '[':
          stack.pop()
  if stack:
    print('no')
  else:
    print('yes')
  sen = sys.stdin.readline().rstrip()