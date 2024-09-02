t = int(input())

def fibo_count(n):
    count0 = [0] * (n+1)
    count1 = [0] * (n+1)

    count0[0] = 1 # fibo(0) = 0이니까 count0 = 1
    count1[0] = 0 # fibo(0) != 1이니까, count1 = 0

    if n > 0:
        count0[1] = 0 # fibo(1) != 0이니까 count0 = 0
        count1[1] = 1 # fibo(1) = 1이니까 count1 = 1
    
    for i in range(2, n+1):
        count0[i] = count0[i-1] + count0[i-2]
        count1[i] = count1[i-1] + count1[i-2]

    return count0, count1

for _ in range(t):
    n = int(input())
    count0, count1 = fibo_count(n)
    print(count0[n], count1[n])