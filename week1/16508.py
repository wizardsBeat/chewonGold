import sys
input = sys.stdin.readline
from collections import Counter

# 주어진 문자열에서 목표 단어를 만들 수 있는지 확인하는 함수
def check(string):
    # 목표 단어의 각 알파벳에 대해
    for t in target:
        # 알파벳이 Counter에 존재하고, 빈도가 0이 아닌 경우
        if t in string and string[t] != 0:
            string[t] -= 1 # 해당 알파벳의 빈도를 감소
        else:
            return False # 알파벳이 부족하거나 존재하지 않으면 False 반환
    return True # 모든 알파벳이 충분하면 True 반환

target = input().strip() # 목표 단어
N = int(input()) # 책의 개수
prices = [] # 책 정보를 저장할 리스트

# 각 책의 가격과 제목을 읽어서 리스트에 저장
for n in range(N):
    price, title = map(str, input().strip().split())
    prices.append([int(price), Counter(title)]) # 가격과 제목의 알파벳 빈도 계산 결과를 저장

# 초기 결과값은 무한대로 설정
result = float('inf')

# 모든 가능한 책 조합을 탐색 (2^N개의 조합)
for i in range(1 << N):
    price = 0
    alpha = Counter() # 현재 조합에서 알파벳의 빈도

    # 현재 조합에 포함된 책들에 대해
    for j in range(N):
        if (i & (1 << j)): # j번째 책이 현재 조합에 포함된 경우
            price += prices[j][0] # 가격 누적
            alpha += prices[j][1] # 알파벳 빈도 누적
    
    # 현재 조합으로 목표 단어를 만들 수 있는지 확인
    if check(alpha):
        result = min(result, price) # 최소 비용 업데이트

# 결과 출력
print(result if result != float('inf') else -1)