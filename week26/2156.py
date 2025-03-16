# 03.16 PM 9시 테스트 케이스는 풀었지만 반례에 오류가 생김
# 03.16 PM 11시 강의를 찾아보니 다이나믹 프로그래밍을 사용하라고 함
# 03.16 PM 11:40 max 오류 해결
import sys
# 연속 3잔 불가능, 최대 섭취량
def wine_select(n, wines):
    dp = [0 for _ in range(10001)]
    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]
    dp[3] = max(wines[1] + wines[3], max(wines[2]+wines[3], dp[2]))
    for i in range(4, n+1):
        dp[i] = max(wines[i]+wines[i-1]+dp[i-3],max(wines[i]+dp[i-2],dp[i-1]))
    return dp[n]
    


# 포두주 잔의 개수
input = sys.stdin.readline
n = int(input())

# 포도주 리스트
wines = [0 for _ in range(10001)]
for i in range(1,n+1):
    wines[i] = int(input())

# 포도주 최대 섭취량
print(wine_select(n, wines))


