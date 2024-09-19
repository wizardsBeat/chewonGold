arr = input()
stack_le = [] # 왼쪽 괄호
stack_ri = [] # 오른쪽 괄호
stack_l = [] # 레이저
answer = 0

arr_ch = arr.replace('()', '+') # 변형된 array

for i in range (len(arr_ch)):
  if arr_ch[i] == '(':
    stack_le.append(i)
  elif arr_ch[i] == ')':
    stack_ri.append(i)
  else:
    stack_l.append(i)

while stack_ri: # 왼쪽 스택이 하나가 남을 때까지 반복
  temp_r = stack_ri.pop(0)
  count = 0 # 레이저가 쇠막대기를 자른 횟수
  for i in range (len(stack_le)):
    if temp_r < stack_le[i]: # 이때 괄호가 완성됨
      for j in stack_l:
        if stack_le[i-1] < j < temp_r: # 쇠막대기를 자르는 레이저가 있음
          count += 1
      answer += count + 1 # 쇠막대기가 잘린 갯수 = 레이저 개수 + 1
      stack_le.pop(i-1)
      break

count = 0
for i in stack_l:
  if stack_le[0] < i < temp_r: # 마지막 괄호
    count += 1
answer += count + 1

print(answer)
