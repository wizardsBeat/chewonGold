N = int(input())
A = list(map(int, input().split()))

result = [-1] * N
stack = []

for i in range(N):
    # 스택에 뭐가 있을 때, 스택에 저장된 인덱스가 가리키는 값과 현재 값을 비교한다
    # 스택에 저장된 인덱스가 가리키는 값 < 현재 값
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()    # 스택에서 인덱스 꺼내기
        result[idx] = A[i]   # 꺼낸 인덱스 위치에 있는 숫자의 오큰수 = 현재 값
    
    # 스택이 비어있거나, 오큰수가 없는 경우
    # 스택에 현재 인덱스 저장
    stack.append(i)

print(*result)