import sys

input = sys.stdin.readline

n = int(input().strip())
ball = input().strip()

def move(color, dir):
    count = 0
    check = False
    for b in ball[::dir]:
        if b != color and not check:
            check = True
        if b == color and check:
            count += 1
    return count


minmove = min(move('R', 1), move('R', -1), move('B', 1), move('B', -1))
print(minmove)
