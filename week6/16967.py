# 백준 16967번 풀이

H, W, X, Y = map(int, input().split())

# 배열 B
B = [list(map(int, input().split())) for _ in range(H + X)]

# 배열 A 초기화
A = [[0] * W for _ in range(H)]

# 배열 A 복원
for i in range(H):
    for j in range(W):
        # 겹치지 않는 부분
        if i < X or j < Y:
            A[i][j] = B[i][j]
        # 겹치는 부분
        else:
            A[i][j] = B[i][j] - A[i - X][j - Y]

# 배열 A 출력
for arr in A:
    print(*arr)
    