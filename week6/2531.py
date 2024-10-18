import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
chobab = []
for _ in range(N):
    chobab.append(int(input().strip()))

chobab += chobab #리스트를 두 번 반복시키기
count = 0
maxNum = 0
for i in range(N):
    chobabnum = len(set(chobab[i:i+k])) #연속으로 먹을 수 있는 초밥 종류 확인
    coupon = c in chobab[i:i+k] #만약 연속으로 먹은 초밥 중에서 쿠폰으로 먹을 수 있는 종류가 있다면
    if not coupon:
        chobabnum += 1
    maxNum = max(maxNum, chobabnum)

print(maxNum)