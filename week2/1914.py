n = int(input()) # 원판의 수 

def hanoi(n, start, end, temp):
    # n = 원판의 수
    # start = 현재 원판이 위치한 장대
    # end = 원판을 옮길 목표 장대
    # temp = 중간 장대 

    if n == 1: # 원판의 수가 1개라면 start에서 바로 end로 옮긴다
        print(start, end)
    else:
        hanoi(n-1, start, temp, end) # n-1개의 원판을 start에서 temp로 옮기기
        print(start, end) # n번째 원판을 start에서 end로 옮기는 걸 출력 
        hanoi(n-1, temp, end, start) # n-1개의 원판을 temp에서 end로 옮기기

def solve_hanoi(n):
    total_moves = 2**n - 1 # 최소 이동 횟수 = 2^n - 1
    print(total_moves)
    if n <= 20:
        hanoi(n, 1, 3, 2)

solve_hanoi(n)