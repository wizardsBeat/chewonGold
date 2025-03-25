import sys

input = sys.stdin.readline

# N = 사다리 수, M = 뱀 수
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

# 게임 시작 위치
state = 1
step = 0

# 게임 진행
while state < 100:
    # 주사위 값 1부터 6까지 각각 계산
    max_position = 0
    for dice in range(1, 7):
        if state + dice <= 100:  # 100을 넘지 않도록
            max_position = max(max_position, num[state + dice])

    # 가장 좋은 위치로 이동
    state = max_position
    step += 1

# 결과 출력
print(step)
