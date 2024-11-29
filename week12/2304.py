import sys

n = int(sys.stdin.readline())  # 기둥의 개수
arr = []

# 입력 받기
for _ in range(n):
    l, h = map(int, sys.stdin.readline().split())
    arr.append((l, h))

# 위치로 정렬
arr.sort(key=lambda x: x[0])

# 가장 높은 기둥 찾기
max_height = max(arr, key=lambda x: x[1])[1]

# 왼쪽에서부터 면적 계산
current_height = 0
last_position = arr[0][0]
width = 0

for pos, height in arr:
    if height > current_height:
        width += current_height * (pos - last_position)
        current_height = height
        last_position = pos

# 오른쪽에서부터 면적 계산
current_height = 0
last_position = arr[-1][0]

for pos, height in reversed(arr):
    if height > current_height:
        width += current_height * (last_position - pos)
        current_height = height
        last_position = pos

# 가장 높은 기둥의 면적 추가
width += max_height

print(width)