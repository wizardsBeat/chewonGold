# 로프의 개수
n = int(input())

# 중량 한계
ropes = [int(input()) for _ in range(n)]

# 내림차순 정렬
ropes.sort(reverse=True)

# 각 로프를 사용할 때의 최대 중량 계산
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (i + 1))

print(max_weight)
