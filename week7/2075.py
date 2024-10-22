import heapq
# 힙에 추가시 자동 정렬 해주기 때문에 heap 사용
heap = []
N = int(input())

for _ in range(N):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(heap) < N:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                #가장 작은거 pop
                heapq.heappop(heap)
                #number push
                heapq.heappush(heap, number)

print(heap[0])