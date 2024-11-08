import sys
input = sys.stdin.readline

s = list(input().strip())


one = int(s.count('1') / 2)
zero = int(s.count('0') / 2)

#0은 뒤에서부터 삭제
for i in range(zero):
    for j in range(len(s)-1,-1,-1):
        if s[j] == '0':
            s.pop(j)
            break

#1은 앞에서부터 삭제
for i in range(one):
    for j in range(len(s)):
        if s[j] == '1':
            s.pop(j)
            break

print(''.join(s))
