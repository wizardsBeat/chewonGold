N = int(input())

option = [[0] * (N+1) for _ in range(N+1)]  # 단축키 있는 위치 저장
stream = [''] * (N+1)  # 원본 단어 저장
m = ''  # 이미 단축키로 지정된 문자들

for i in range(N):
    stream[i] = input()
    words = list(stream[i].split())
    
    for j, word in enumerate(words):
        if word[0].lower() not in m:
            option[i][j] = 1  # 단축키 지정된 단어 위치 표시
            m += word[0].lower()
            break  # 단축키는 한 단어에만 지정되므로 한 번 지정 후 루프를 빠져나옴

print(m)
print(option)