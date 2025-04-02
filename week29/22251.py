import sys
from itertools import product

# 0~9까지 7-세그먼트 점등 패턴 (인덱스는 숫자, 값은 점등된 LED 비트)
SEGMENTS = [
    0b1111110,  # 0
    0b0110000,  # 1
    0b1101101,  # 2
    0b1111001,  # 3
    0b0110011,  # 4
    0b1011011,  # 5
    0b1011111,  # 6
    0b1110000,  # 7
    0b1111111,  # 8
    0b1111011   # 9
]

def count_differences(a, b):
    """ 두 숫자의 7-세그먼트 패턴 차이를 계산 """
    return bin(SEGMENTS[a] ^ SEGMENTS[b]).count('1')

def solve(n, k, p, x):
    current_digits = list(map(int, str(x).zfill(k)))  # 현재 층의 K자리
    count = 0
    
    for num in range(1, n + 1):
        if num == x:
            continue  # 자기 자신 제외
        target_digits = list(map(int, str(num).zfill(k)))
        
        # 자리별 차이 계산
        diff = sum(count_differences(current_digits[i], target_digits[i]) for i in range(k))
        
        if diff <= p:
            count += 1
    
    return count

# 입력
n, k, p, x = map(int, sys.stdin.readline().split())
print(solve(n, k, p, x))
