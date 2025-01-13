import sys
input = sys.stdin.readline

n, k = map(int, input().split())

table = list(input().strip())
answer = 0

def ham(num):
    global answer
    start = num - k
    if start < 0 :
        start = 0
    end = num +k
    if end >= len(table):
        end = len(table) -1
    for i in range(start, end+1):
        if table[i] == 'H':
            table[i] = ''
            answer += 1
            break
    return

for i in range(len(table)):
    if table[i] == 'P':
        ham(i)
print(answer)