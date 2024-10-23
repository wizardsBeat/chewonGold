n = int(input())

alphabet = []

for _ in range(n):
    words = list(input().split())
    hasKey = False
    for i in range(len(words)):
        if words[i][0].upper() not in alphabet:
            alphabet.append(words[i][0].upper())
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            hasKey = True
            print(' '.join(words))
            break
        
    if hasKey == False:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j].upper() not in alphabet:
                    alphabet.append(words[i][j].upper())
                    words[i] = words[i][:j] + "[" + words[i][j] + "]" + words[i][j+1:]
                    hasKey = True
                    print(' '.join(words))
                    break
            if hasKey:
                break
    
    if hasKey == False:
        print(' '.join(words))