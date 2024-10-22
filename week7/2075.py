N = int(input())  # N 입력 받기

# N번째 큰 수들을 저장할 리스트
largest_numbers = []

# 전체 데이터를 한 줄씩 입력받음
for i in range(N):
    num_list = list(map(int, input().split()))  # 한 줄씩 입력받음

    # 입력받은 숫자들을 차례대로 처리
    for num in num_list:
        # 리스트가 아직 N개 미만이면 그냥 추가
        if len(largest_numbers) < N:
            largest_numbers.append(num)
            largest_numbers.sort()  # 정렬하여 가장 작은 값이 맨 앞에 오도록 유지
        else:
            # 리스트가 이미 N개라면, 가장 작은 값보다 큰 경우에만 추가
            if num > largest_numbers[0]:
                largest_numbers[0] = num  # 가장 작은 값을 새 값으로 대체
                largest_numbers.sort()    # 다시 정렬하여 가장 작은 값이 맨 앞에 오도록 유지

# N번째 큰 수는 정렬된 리스트에서 가장 작은 값이므로 첫 번째 값이 됨
print(largest_numbers[0])
