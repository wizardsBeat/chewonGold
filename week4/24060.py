import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 병합 정렬 = 쪼개서 정렬하기
def merge_sort(A, p, r, K): # 배열 A[p..r], K번째로 저장된 값 찾기
    if p < r:    # 시작 인덱스(p)가 끝 인덱스(r)보다 작을 때 = 배열에 최소 2개 이상의 원소가 있을 때 
        q = (p+r) // 2    # q = 중간 지점
        merge_sort(A, p, q, K)    # A[p..q] = 왼쪽 부분 정렬
        merge_sort(A, q+1, r, K)  # A[q+1..r] = 오른쪽 부분 정렬
        merge(A, p, q, r, K)      # 쪼갠 거 합치기

# 쪼갠거 합치기 
def merge(A, p, q, r, K):
    global count, result    # 저장 횟수, K번째 저장된 값
    tmp = []    # 병합할 데이터를 저장하는 임시 리스트

    i = p    # A[p..q] 왼쪽 부분에서 첫번째 원소 인덱스
    j = q+1  # A[q+1..r] 오른쪽 부분에서 첫번째 원소 인덱스
    
    # 왼쪽 부분, 오른쪽 부분 각각 원소 비교
    while i <= q and j <= r:
        # 왼쪽 부분 원소가 오른쪽 부분 원소보다 작거나 같으면 왼쪽 원소 저장
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1    # 왼쪽 부분에서 다음 원소 인덱스로
        else:
        # 오른쪽 부분 원소가 왼쪽 부분 원소보다 작으면 오른쪽 원소 저장
            tmp.append(A[j])
            j += 1    # 오른쪽 부분에서 다음 원소 인덱스로
    
    # 왼쪽 부분에만 원소가 남아있을 때, 남은 거 모두 임시 리스트에 넣기
    while i <= q:
        tmp.append(A[i])
        i += 1

    # 오른쪽 부분에만 원소가 남아있을 때, 남은 거 모두 임시 리스트에 넣기
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    # 정렬된 거(tmp)를 원래 배열 A에 복사하기
    for t in range(len(tmp)):
        A[p+t] = tmp[t]
        count += 1    # 저장할 때마다 횟수 카운팅

        if count == K:    # 저장 횟수가 K만큼 되면
            result = A[p+t]    # 그 값을 결과에 저장하기

count = 0    # 저장 횟수
result = -1  # K번째 저장된 값, 디폴트가 -1 = 없으면 -1 출력

merge_sort(A, 0, N-1, K)    # 배열 A를 0 ~ N-1 (전체) 병합 정렬
print(result)