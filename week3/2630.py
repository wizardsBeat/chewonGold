# 백준 2630번 풀이

N = int(input()) # 전체 종이 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)] # N*N 색종이 입력
result = [] # 잘린 색종이의 결과 담을 리스트

def slice(x, y, n) : # 시작점 좌표 (x, y), n은 입력받은 색종이 크기
  color = paper[x][y] # 현재 영역의 첫 번째 색(가장 왼쪽 위) 저장

  # 시작점을 기준으로 해당 영역이 모두 같은 색으로 이루어졌는지 판단
  for i in range(x, x+n) :
    for j in range(y, y+n) :
      if color != paper[i][j] : # 다른 색이 있을 경우 함수 재귀적 호출
        slice(x, y, n//2) # 왼쪽 위
        slice(x, y+n//2, n//2) # 오른쪽 위
        slice(x+n//2, y, n//2) # 왼쪽 아래
        slice(x+n//2, y+n//2, n//2) # 오른쪽 아래
        return
      
  # 모든 색이 같을 경우 결과에 저장    
  if color == 0 :
    result.append(0) # 흰색 영역
  else :
    result.append(1) # 파란색 영역


slice(0,0,N) # 전체 종이를 시작점부터 분할 시작
print(result.count(0))
print(result.count(1))
