n = int(input())

alphabet = []

for _ in range(n):
    words = list(input().split())
    hasKey = False # 단축키 현재 지정되어 있는지 아닌지 판별하는 bool 변수
    for i in range(len(words)):
        if words[i][0].upper() not in alphabet: #먼저 단어의 첫번째 글자를 단축키로 지정할 수 있는지 확인
            alphabet.append(words[i][0].upper()) #대소문자 구분 없으니 무조건 대문자로 저장
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            hasKey = True # 단축키 지정 되었으니까 hasKey True로 변경
            print(' '.join(words))
            break
        
    if hasKey == False: # 단어의 첫번째 글자를 단축키로 지정할 수 없는 경우
        for i in range(len(words)): # 모든 글자를 순회해야하니까 이중 for문 사용
            for j in range(len(words[i])):
                if words[i][j].upper() not in alphabet:
                    alphabet.append(words[i][j].upper())
                    words[i] = words[i][:j] + "[" + words[i][j] + "]" + words[i][j+1:]
                    hasKey = True  # 단축키 지정 되었으니까 hasKey True로 변경
                    print(' '.join(words))
                    break
            if hasKey: #단축키 지정되면 시간 단축을 위해 break
                break 
    
    if hasKey == False: #단축키 없으면 그냥 출력
        print(' '.join(words))