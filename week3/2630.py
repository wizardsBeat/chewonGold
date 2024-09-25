lines = int(input())
arr = []
whiteslices = 0
blueslices = 0
for _ in range(lines):
    temp = list(map(int, input().split()))
    arr.append(temp)

def cut(x, y, length):
    global whiteslices, blueslices
    color = arr[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if arr[i][j] != color:
                half = length // 2
                cut(x, y, half)
                cut(x, y + half, half)
                cut(x + half, y, half)
                cut(x + half, y + half, half)
                return
    if color == 0:
        whiteslices += 1
    else:
        blueslices += 1

cut(0, 0, lines)
print(whiteslices)
print(blueslices)
