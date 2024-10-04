# 백준 2164번 풀이

from collections import deque

N = int(input())

queue = deque(range(1, N + 1)) # 1번부터 N번까지의 카드 큐에 저장

while len(queue) > 1: # 카드 한 장 남을 때까지 실행
    queue.popleft() # 맨 위에 있는 카드 버림
    move = queue.popleft() # 맨 위에 있는 카드 = 밑으로 갈 카드
    queue.append(move) # 맨 밑으로 카드 옮김

print(queue[0]) # 마지막에 남은 카드 출력
