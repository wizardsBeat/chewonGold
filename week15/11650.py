import sys

input = sys.stdin.readline
N = int(input().strip())
numarr = []
for i in range(N):
    nums = input().strip()
    x, y = nums.split()
    numarr.append([int(x), int(y)])

numarr.sort()

for i in numarr:
    print(i[0], i[1])