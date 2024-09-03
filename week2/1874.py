import sys

input = sys.stdin.readline

stack = []  #빈 스택 만들기

n = int(input()) #숫자 입력

li = [] #리스트 만들기
for i in range(n):  #숫자 입력 후 리스트에 저장
    a = int(input())
    li.append(a)

num = 1     #최근에 스택에 넣은 숫자
ans = []    #정답 + - 저장할 리스트
flag = 1    #출력 가능한지 검사할 flag

for i in li:    #입력받은 숫자 리스트 반복
    while num <= i: #num <= i 일 때는 스택에 + 추가
        ans.append('+')
        stack.append(num)
        num += 1

    if stack[-1] > i:   #스택 맨 위에 있는 값이 i 보다 크면 수열 만들기 불가
        flag = 0

    if stack[-1] == i: #pop #스택 맨 위에 있는 수가 i 와 같으면 pop
        ans.append('-')
        stack.pop()
    
if flag:    #flag == 1이면 수열 만들기 가능
    for i in ans:
        print(i)
else:       #flag == 0이면 수열 만들기 불가능
    print("NO")