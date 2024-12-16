import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
indexlist = [ i for i in range(n+1)]
result = []

idx = 0
k = arr.pop(idx)
result.append(indexlist.pop(idx)+1)


while(len(arr) > 0):
        
    if(k < 0):
        idx = (idx+k) % len(arr)
    else:
        idx = (idx+(k-1))%len(arr)
        
    k = arr.pop(idx)
    result.append(indexlist.pop(idx) + 1)
        
        
print(' '.join(list(map(str, result))))