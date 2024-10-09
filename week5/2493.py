# 백준 2493번 문제 풀이

N = int(input())
top = list(map(int, input().split()))

stack = [] # 높이 비교할 스택
reciever = [] # 수신받는 탑 저장

for i in range(N):
    # 현재 탑의 높이가 더 높을 때까지 스택에서 pop
    while stack and top[stack[-1]] <= top[i]:
        stack.pop()

    if stack:
        # 현재 탑이 신호를 받는 탑 인덱스 저장
        reciever.append(stack[-1] + 1)  # 탑 인덱스는 1부터 시작하므로 더하기 1
    else:
        # 신호를 받는 탑이 없으면 0 저장(미수신: 0)
        reciever.append(0)
    
    # 현재 탑 인덱스를 스택에 추가
    stack.append(i)

print(' '.join(map(str, reciever)))