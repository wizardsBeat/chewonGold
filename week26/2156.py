# 연속 3잔 불가능, 최대 섭취량
def wine_select(n, wines):
    wine_drink = 0
    # 문제 2: 입력이 하나일 대 None이 됨, 해결
    current_max = max(wines)
    current_point = 0
    while(current_point < n//2):
        # 문제 1: 입력이 두 개일 때 None이 됨, 해결
        if n < 3:
            current_max = wines[0] + wines[1]
            break
        for i in range(n):
            point = current_point + i
            if (point + 1) % 3 == 0:
                pass
            else:
                wine_drink += wines[point]
                print(f'바뀐값: {wine_drink}')
        if wine_drink > current_max:
            current_max = wine_drink
        wine_drink = 0
        current_point += 1
    return current_max
            

# 포두주 잔의 개수
n = int(input())

# 포도주 리스트
wines = []
for _ in range(n):
    wines.append(int(input()))
print(f'포도주들: {wines}')

# 포도주 최대 섭취량
print(f'최대 섭취량: {wine_select(n, wines)}')


