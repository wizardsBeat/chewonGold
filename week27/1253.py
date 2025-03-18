import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

for i in range(n):
    target = arr[i]
    start, end = 0, n - 1

    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        total = arr[start] + arr[end]

        if total == target:
            answer += 1
            break
        elif total < target:
            start += 1
        else:
            end -= 1

print(answer)
