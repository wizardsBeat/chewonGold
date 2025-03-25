from collections import deque

# 입력
N, M = map(int, input().split())

# 1부터 100까지의 번호 초기화
num = [i for i in range(101)]

# 사다리 입력
for _ in range(N):
    N_input, N_output = map(int, input().split())
    num[N_input] = N_output

# 뱀 입력
for _ in range(M):
    M_input, M_output = map(int, input().split())
    num[M_input] = M_output

# BFS를 위한 큐
queue = deque([1])  # 시작은 1번 칸
visited = [False] * 101
visited[1] = True
step = 0

# BFS 시작
while queue:
    size = len(queue)
    for _ in range(size):
        state = queue.popleft()

        # 1부터 6까지 주사위 값을 던져보며 진행
        for dice in range(1, 7):
            next_state = state + dice
            if next_state <= 100:
                next_state = num[next_state]  # 사다리나 뱀을 타고 이동

                if next_state == 100:  # 100에 도달하면 끝
                    print(step + 1)
                    exit()

                if not visited[next_state]:
                    visited[next_state] = True
                    queue.append(next_state)

    step += 1

# 결과 출력
print(step)
