n = int(input().strip())
numarr = list(map(int, input().split()))

increase = []

for num in numarr:
    if not increase or num > increase[-1]:
        increase.append(num)
    else:
        for i in range(len(increase)):
            if increase[i] >= num:
                increase[i] = num
                break

print(len(increase))
