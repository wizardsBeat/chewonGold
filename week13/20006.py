import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    lev, name = input().split()
    lev = int(lev)
    flag = False
    for room in rooms:
        key = room[0][0]
        if abs(key - lev) <= 10:
            if len(room) < m:
                room.append((lev, name))
                flag = True
                break
    if not flag:
        rooms.append([(lev, name)])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)