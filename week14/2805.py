import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))
maxtree = max(trees)
treecutting = []

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        cutting = 0
        for tree in arr:
            if tree > mid:
                cutting += tree - mid
        
        if cutting == target:
            treecutting.append(mid)
            return mid
        elif cutting < target:
            end = mid - 1
        else:
            treecutting.append(mid)
            start = mid + 1
    return None
        
binary_search(trees, m, 0, maxtree)
print(max(treecutting))