# 문장 입력 받기
stream = list(input())

# 최대 글자
if len(stream) >= 600000:
    stream = stream[:600000]
# print(stream)

# 위치를 알려줄 커서
cursor = len(stream)+1

# 명령어 입력
for _ in range(int(input())):
    c = input().split(' ')
    # print(cursor)
    if c[0] == 'L':
        if cursor > 0:
            cursor -= 1
    if c[0] == 'D':
        if cursor < len(stream):
            cursor += 1
    if c[0] == 'B':
        if cursor > 0:
            if cursor > len(stream):
                del stream[cursor-2]
            else:
                del stream[cursor-1]
            cursor -= 1
    if c[0] == 'P':
        stream.insert(cursor, c[1])


print(''.join(stream))
        