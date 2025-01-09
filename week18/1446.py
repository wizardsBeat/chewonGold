import sys

input = sys.stdin.readline

# N = 지름길 수, D는 고속도로 길이
N, D = map(int, input().split())
lines = []

# 지름길 리스트
for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D and length < end - start:  # 유효한 지름길만 추가
        lines.append((start, end, length))

# 거리 테이블 초기화
dist = [i for i in range(D + 1)]

# DP 방식으로 최단 거리 구하기
for i in range(D + 1):
    # 기본 도로로 한 칸 이동
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)
    
    # 지름길 적용
    for start, end, length in lines:
        if i == start and end <= D:
            dist[end] = min(dist[end], dist[start] + length)

# 결과 출력
print(dist[D])
