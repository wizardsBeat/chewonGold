from collections import defaultdict

n = int(input().strip())
fruits = list(map(int, input().strip().split()))

def tangtang(fruits):
    n = len(fruits)
    left = 0
    fcount = defaultdict(int)
    answer = 0

    for right in range(n):
        fcount[fruits[right]] += 1

        while len(fcount) > 2:
            fcount[fruits[left]] -= 1
            if fcount[fruits[left]] == 0:
                del fcount[fruits[left]]
            left += 1

        answer = max(answer, right - left + 1)

    return answer

print(tangtang(fruits))
