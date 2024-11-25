n, k = map(int, input().split())

numbers = list(map(int, input().split()))

sumnum = 0
nj = [0]
sumlist = []
for i in range(n):
    sumnum += numbers[i]
    nj.append(sumnum)

for i in range(n-k+1):
    sumlist.append(nj[i+k] - nj[i])
    
print(max(sumlist))