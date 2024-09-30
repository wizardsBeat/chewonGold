import sys
from collections import Counter

n = int(sys.stdin.readline())
nc = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mc = list(map(int, sys.stdin.readline().split()))

card = {num: 0 for num in mc} # 정답 리스트에 있는 숫자들에 모두 0을 할당하여 딕셔너리 생성
mc_set = set(mc) # list에서 찾을때는 매 순회마다 O(N)의 시간이 필요, set인 경우 해시 테이블로 구현되어 있으므로 O(N)

for i in nc: # 상근이가 가지고 있는 카드 중에서
  if i in mc_set: # mc_set에 값이 있다면
    card[i] += 1 # 정답 리스트에 개수를 추가

answer = [str(card[num]) for num in mc] # mc를 순회하며 해당하는 값 호출

print(' '.join(answer))