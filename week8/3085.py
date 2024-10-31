import sys
input = sys.stdin.readline

N = int(input().strip())
candy = []
for i in range(N):
    candy.append(list(input().strip()))

def check_row(arr, row): # 연속되는 사탕 개수 세기
    max_count = 1
    count = 1
    for j in range(1, N):
        if arr[row][j] == arr[row][j-1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count

def check_col(arr, col):
    max_count = 1
    count = 1
    for i in range(1, N):
        if arr[i][col] == arr[i-1][col]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count

answer = 0

for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j + 1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            # 교환된 행과 열만 검사
            answer = max(answer, check_row(candy, i), check_col(candy, j), check_col(candy, j+1))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        # 아래와 교환
        if i + 1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            # 교환된 행과 열만 검사
            answer = max(answer, check_row(candy, i), check_row(candy, i+1), check_col(candy, j))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(answer)
