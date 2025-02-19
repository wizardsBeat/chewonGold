import sys
sys.setrecursionlimit(100000)

s = input().strip()
t = input().strip()
answer = 0

def recurse(T):
    global answer
    if T == s:
        answer = 1
        return
    if len(T) <= len(s):
        return

    if T[-1] == 'A':  
        recurse(T[:-1])

    if T[0] == 'B':  
        recurse(T[::-1][:-1])

recurse(t)
print(answer)
