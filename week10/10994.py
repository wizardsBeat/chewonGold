N = int(input().strip())

M = 4*N -3
stars = [[' ']*M for _ in range(M)]

def stardraw(n, idx):
    starlen = 4*n -3
    if n == 1:
        stars[idx][idx] = '*'
        return
    
    for i in range(idx, idx+starlen):
        stars[idx][i] = '*' # 첫째줄
        stars[idx+starlen-1][i] = '*' #마지막줄
        stars[i][idx] = '*' # 왼쪽줄
        stars[i][idx+starlen-1]='*' #오른쪽줄

    return stardraw(n-1, idx+2)

stardraw(N,0)

for i in range(M):
    for j in range(M):
        print(stars[i][j],end="")
    print()
    