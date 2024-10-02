T = int(input())

dp_cache = [0] * 11
dp_cache[1] = 1
dp_cache[2] = 2
dp_cache[3] = 4

for i in range(4, 11):
    dp_cache[i] = dp_cache[i-1] + dp_cache[i-2] + dp_cache[i-3]

for _ in range(T):
    print(dp_cache[int(input())])