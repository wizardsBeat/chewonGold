import heapq

N = int(input())  # N 입력 받기

heap = []

for _ in range(N):
    num_list = list(map(int, input().split()))  # 한 줄씩 숫자 입력받기
    for num in num_list:
        if len(heap) < N:
            heapq.heappush(heap, num)  # 힙이 N개보다 작으면 추가
        else:
            if num > heap[0]:  # 새로운 숫자가 힙의 최소값보다 크면 교체
                heapq.heapreplace(heap, num)

# 힙에 남은 값 중 가장 작은 값이 전체에서 N번째 큰 값
print(heap[0])
