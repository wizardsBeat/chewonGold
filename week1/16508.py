
# 단어별 빈도수 계산을 위해 사용
from collections import Counter

def check(string):
    for t in target:
        if t in string and string[t] != 0:
            string[t] -= 1
        else:
            return False
    return True

# 만들고자 하는 단어
target = input().strip()
# 책의 수
N = int(input())
prices = []

for n in range(N):
    price, title = map(str, input().strip().split())
    prices.append([int(price), Counter(title)])

# 초기값을 무한대로 설정
result = float('inf')

# 2^N개의 조합을 탐색
for i in range(1<<N): # 2^N = 1 << N
    price = 0
    alpha = Counter()
    # 현재 책이 현재 조합에서 선택되었는지 확인
    for j in range(N):
        if (i & 1 << j): # 뒤에서부터 연산 i & (1 << j), i의 j번째 비트가 1인지 확인
            price += prices[j][0] # 책의 가격을 더함
            alpha += prices[j][1] # 책 제목의 알파벳을 더함

    if check(alpha): # 선택된 책들로 단어를 만들 수 있는지 확인
        result = min(result, price) # 최소비용 갱신

print(result if not result == float('inf') else -1)