N = int(input())  # 입력받을 옵션 개수
m = ''  # 이미 단축키로 지정된 문자들
stream = []  # 옵션들을 저장할 리스트

for i in range(N):
    words = input().split()  # 옵션을 단어로 분리
    shortcut_assigned = False  # 단축키가 지정되었는지 여부
    
    # 1. 각 단어의 첫 글자를 우선적으로 단축키로 지정 시도
    for j, word in enumerate(words):
        if word[0].lower() not in m:  # 첫 글자가 단축키로 사용되지 않았다면
            words[j] = '[' + word[0] + ']' + word[1:]  # 첫 글자에 단축키 지정
            m += word[0].lower()  # 사용된 단축키 기록
            shortcut_assigned = True  # 단축키 지정 완료
            break  # 단축키가 지정되었으므로 루프 종료
    
    # 2. 첫 글자가 모두 사용된 경우, 단어의 다른 글자에서 단축키 지정
    if not shortcut_assigned:
        for j, word in enumerate(words):
            for a in range(1, len(word)):  # 단어의 첫 글자를 제외한 나머지 글자 탐색
                if word[a].lower() not in m:  # 사용되지 않은 글자를 찾음
                    words[j] = word[:a] + '[' + word[a] + ']' + word[a+1:]  # 단축키로 지정
                    m += word[a].lower()  # 사용된 단축키 기록
                    shortcut_assigned = True  # 단축키 지정 완료
                    break  # 단축키 지정 후 루프 종료
            if shortcut_assigned:
                break
    
    # 단어 리스트를 다시 문자열로 합쳐서 stream에 저장
    stream.append(' '.join(words))

# 출력
print('\n'.join(stream))  # 수정된 문장 출력
