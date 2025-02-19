n, c = map(int, input().split())
messages = list(map(int, input().split()))
answer = []
numdict = {}
order = 0
for mes in messages:
    if mes in numdict:
        numdict[mes][0] += 1
    else:
        numdict[mes] = [1, order]
        order += 1

sorteddict = sorted(numdict.items(), key = lambda x: (-x[1][0], x[1][1]))
for num, (cnt, number) in sorteddict:
    answer += [num] * cnt

print(*answer)