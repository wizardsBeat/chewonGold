import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
result = [-1] * n  # 결과를 저장할 리스트를 -1로 초기화
stack = []  # 스택 초기화

for i in range(n):
    # 스택이 비어있지 않고, 현재 수가 스택의 인덱스 값보다 크면
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    # 현재 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(*result)
