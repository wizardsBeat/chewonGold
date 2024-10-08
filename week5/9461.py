# 규칙을 통해서 계산한 결과
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65

T = int(input())
df = [0] * 101
# 우선 초기화
df[1] = 1
df[2] = 1
df[3] = 1
df[4] = 2
df[5] = 2
for i in range(6, 101):
    df[i] = df[i - 5] + df[i - 1]
for _ in range(T):
    print(df[int(input())])