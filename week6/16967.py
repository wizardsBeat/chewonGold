import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B = []
for _ in range(H + X):
    B.append(list(map(int, input().split())))

for i in range(X, H):
    for j in range(Y, W):
        B[i][j] = B[i][j] - B[i-X][j-Y] #  Bi,j = Ai,j + Ai-X,j-Y 이거니까 B에서 그걸 빼주는 작업을 하는 것

for i in B[:H]:
    print(*i[:W]) #2차원 배열 slicing