P = [0,1,1,1,2,2,3,4,5,7,9]
#파도반 수열 P[N] = P[N-2] + P[N-3]

def wave(x):
    if x < len(P):
        return P[x]
    
    for i in range(len(P), x+1):
        P.append(P[i - 2] + P[i - 3])
    
    return P[x]

T = int(input())
answer = []
for i in range(T):
    N = int(input())
    answer.append(str(wave(N)))

print('\n'.join(answer))