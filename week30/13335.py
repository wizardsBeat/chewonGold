from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
time = 0
current_weight = 0

while trucks or current_weight > 0:
    time += 1

    exited_truck = bridge.popleft()
    current_weight -= exited_truck

    if trucks:
        if current_weight + trucks[0] <= L:
            new_truck = trucks.popleft()
            bridge.append(new_truck)
            current_weight += new_truck
        else:
            bridge.append(0)

print(time)
