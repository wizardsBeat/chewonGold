# 하노이의 탑

N = int(input())

move = 2**N - 1 # 원판이 N개일 때 2^n - 1번 이동하면 모든 원판을 옮길 수 있음

def hanoi_tower (N, start, end):
  if N == 1: # n=1일 때 재귀 함수를 끝냄
    print (start, end)
    return
  
  # start에서 n-1개의 원판을 보조 기둥으로 보냄 (기둥 숫자의 총합이 6이므로 start와 end를 제외한 보조 기둥의 번호는 6-start-end)
  hanoi_tower(N-1, start, 6 - end - start)
  print (start, end) # 옮겨진 과정 출력
  # 보조 기둥의 원판을 end로 보냄 
  hanoi_tower(N-1, 6-start-end, end)

print(2**N-1)
if N <= 20: # N이 20을 초과할 때는 과정을 출력할 필요가 없으므로
  hanoi_tower(N, 1, 3)
