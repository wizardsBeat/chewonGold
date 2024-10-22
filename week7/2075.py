N = int(input())  # N 입력 받기

M = []
for i in range(N):
    num = list(map(int, input().split()))  # 숫자를 입력받아서 리스트로 변환
    M.extend(num)  # 전체 리스트 M에 숫자를 추가 (2차원 배열 -> 1차원 배열)

M = sorted(M, reverse=True)  # 전체 리스트를 내림차순 정렬

print(M[N-1])  # N번째 큰 수 출력 (N번째 큰 수이므로 인덱스는 N-1)
