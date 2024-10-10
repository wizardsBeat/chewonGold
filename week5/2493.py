import sys

input = sys.stdin.readline

N = int(input().strip())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack and tower[i] >= tower[stack[-1]]:
        stack.pop()
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1] + 1)
    stack.append(i)

print(" ".join(map(str, answer)))
