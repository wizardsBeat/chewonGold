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

p_op = options.values() # 조건에 해당하는 값을 저장

for _ in range (M):
  power = int(sys.stdin.readline())

  for p in p_op:
    if power <= p:
      print(options_power[p])
      break