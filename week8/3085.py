import sys

def check_candy(candy, N, board):
  max_cnt = 0

  # 가로
  for i in range (N):
    cnt = 0
    flag = False
    for j in range (N):
      if board[i][j] == candy:
        cnt += 1
      else:
        if flag:
          if max_cnt < cnt: # 이미 한 번 교환했으므로 한 번 더 다른 사탕을 만나면 거기서 종료
            max_cnt = cnt
          cnt, flag = 0, False # 초기화

        elif i < N-1 and board[i+1][j] == candy: # 아래와 교환 가능한 경우
          cnt += 1
          flag = True
        
        elif i > 0 and board[i-1][j] == candy: # 위와 교환 가능한 경우
          cnt += 1
          flag = True
        
        else: # 교환 불가
          if j < N-1 and board[i][j+1] == candy: # 오른쪽과 교환 가능한 경우
            cnt += 1
          if max_cnt < cnt:
            max_cnt = cnt
          cnt, flag = 0, False # 초기화

    if max_cnt < cnt:
      max_cnt = cnt
    
  # 세로
  for i in range (N):
    cnt = 0
    flag = False
    for j in range (N):
      if board[j][i] == candy:
        cnt += 1
      else:
        if flag:
          if max_cnt < cnt:
            max_cnt = cnt
          cnt, flag = 0, False

        elif i < N-1 and board[j][i+1] == candy: # 오른쪽과 교환 가능한 경우
          cnt += 1
          flag = True
        
        elif i > 0 and board[j][i-1] == candy: # 왼쪽과 교환 가능한 경우
          cnt += 1
          flag = True
        
        else:
          if j < N-1 and board[j+1][i] == candy:
            cnt += 1
          if max_cnt < cnt:
            max_cnt = cnt
          cnt, flag = 0, False # 초기화

    if max_cnt < cnt:
      max_cnt = cnt
  
  return max_cnt
          

N = int(sys.stdin.readline()) # size of board
sc = -1 # short cut
board = []
candies = []
max_cnt = 0 # 먹을 수 있는 최대 사탕 개수

# fill up board
# C: red, P: blue, Z: green, Y: yellow
for _ in range (N):
  row = list(sys.stdin.readline().strip())
  board.append(row)
  sr = set(row)
  candies.extend(sr)
  if len(sr) == 1: # 모든 줄이 하나의 사탕으로 이루어져 있을 때 무조건 이값이 최대
    sc = N

candies = list(set(candies))

if sc == N: # 빠른 정답 체크
  print(N)
else:
  ans = []
  for candy in candies:
    ans.append(check_candy(candy, N, board))
  
  print(max(ans))