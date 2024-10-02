T = int(input())

def dp(n):
    if n >= 4:
        return dp(n-1)+dp(n-2)+dp(n-3)
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

for _ in range(T):
    print(dp(int(input())))