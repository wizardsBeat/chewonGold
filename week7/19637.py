import sys

N, M = map(int, sys.stdin.readline().split())
options = {} # key가 칭호 이름
options_power = {} # key가 power

for _ in range (N):
  option, value = sys.stdin.readline().split()
  value = int(value)
  if value not in options.values(): # 앞에 동일한 조건이 있었다면 뒤의 조건은 처리되지 않으므로 조건에 넣지 않아도 됨
    options[option] = value

for key, value in options.items():
  options_power[value] = key # key와 value 값을 반대로 저장

p_op = list(options.values()) # 조건에 해당하는 값을 저장

for _ in range (M):
  power = int(sys.stdin.readline())

  left = 0
  right = len(p_op)
  
  while True:
    mid = (left+right)//2
    if power > p_op[mid]:
      if power <= p_op[mid+1]: # 조건 만족 (해당하는 칭호가 없는 전투력은 주어지지 않으므로 mid+1이 range를 벗어날 수 없음)
        print(options_power[p_op[mid+1]])
        break
      else: # left의 값이 더 커져야함
        left = mid
    else: # power <= p_op[mid]
      if mid == 0:
        print(options_power[p_op[0]])
        break
      else:
        if p_op[mid-1] < power: # 조건 만족
          print(options_power[p_op[mid]])
          break
        else:
          right = mid # right의 값이 더 작아져야함