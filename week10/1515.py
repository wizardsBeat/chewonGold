N = list(input())
num = 1

while len(N) > 0:
    numstring = str(num)
    
    for digit in numstring:
        if len(N) > 0 and N[0] == digit:
            N.pop(0)
    
    num += 1

print(num - 1)
