import sys
from collections import Counter

input = sys.stdin.readline

size = int(input())
N = sorted(int(input()) for _ in range(size))

# 산술 평균
print(round(sum(N) / size))

# 중앙값
print(N[size // 2])

# 최빈값
count = Counter(N).most_common()  # 빈도수 높은 순으로 정렬된 리스트 반환
max_freq = count[0][1]  # 가장 높은 빈도수
modes = sorted([num for num, freq in count if freq == max_freq])  # 빈도수가 같은 값들 정렬

if len(modes) > 1:
    print(modes[1])  # 두 번째로 작은 최빈값
else:
    print(modes[0])  # 최빈값이 하나일 경우

# 범위
print(N[-1] - N[0])
