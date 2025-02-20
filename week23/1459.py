x,y,w,s = map(int, input().split())

time = 0
if 2 * w <= s:
    print((x+y)*w)
else:
    small = min(x,y)
    time = small*s
    absxy = abs(x-y)
    if w > s:
        if absxy % 2 == 0:
            time += absxy * s
        else:
            time +=  (absxy-1) * s + w
    else:
        time += absxy*w
    print(time)