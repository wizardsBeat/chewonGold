import sys

text = input()
N = len(text)
M = int(input())
command_list = [0] * M
for i in range (M):
  command_list[i] = sys.stdin.readline().strip()

cursor = N # 커서 위치

def read_command(text, command, cursor, N):
  if command == "L":
    if cursor != 0: # 커서가 문장의 맨 앞일 때 제외
      cursor -= 1
  elif command == "D":
    if cursor != N: # 커서가 문장의 맨 뒤일 때 제외
      cursor += 1
  elif command == "B":
    if cursor != 0: # 커서가 문장의 맨 앞일 때 제외
      if cursor == 1:
        text = text[1:]
      elif cursor == N:
        text = text[:N-1]
      else:
        text = text[:cursor-1] + text[cursor:]
      cursor -= 1
  else:
    text = text[:cursor] + command[2] + text[cursor:]
    cursor += 1
  return text, cursor

for command in command_list:
  text, cursor = read_command(text, command, cursor, len(text))

print(text)
