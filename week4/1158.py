N, K = map(int, input().split())

queue = list(range(1, N + 1)) # queue 형태로 만들기
answer = []
index = 0

while queue:
    index = (index + K - 1) % len(queue) #index 1부터 시작해서 K에서 1 빼준게 인덱스
    answer.append(queue.pop(index)) 
print('<' + ", ".join(map(str, answer)) + '>')
