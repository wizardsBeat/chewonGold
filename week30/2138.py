def toggle(state, idx):
    for i in [idx - 1, idx, idx + 1]:
        if 0 <= i < len(state):
            state[i] = 1 - state[i]

def solve(N, start, target):
    def try_case(first_pressed):
        temp = start[:]
        cnt = 0

        if first_pressed:
            toggle(temp, 0)
            cnt += 1

        for i in range(1, N):
            if temp[i - 1] != target[i - 1]:
                toggle(temp, i)
                cnt += 1

        if temp == target:
            return cnt
        else:
            return float('inf')

    result = min(try_case(False), try_case(True))
    return result if result != float('inf') else -1

# 입력
N = int(input())
start = list(map(int, input().strip()))
target = list(map(int, input().strip()))

# 출력
print(solve(N, start, target))
