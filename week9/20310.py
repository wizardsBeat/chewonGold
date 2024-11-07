import sys

s = list(sys.stdin.readline().rstrip())

n = s.count('0')
m = s.count('1')

# 앞에서부터 '1'을 m // 2 만큼 제거
check = 0
i = 0
while check < m // 2 and i < len(s):
    if s[i] == '1':
        s.pop(i)
        check += 1
        # pop()으로 요소를 제거하면 리스트가 앞으로 당겨지므로 i를 증가시키지 않음
    else:
        i += 1  # '1'이 아닌 경우에만 다음 인덱스로 이동

# 뒤에서부터 '0'을 n // 2 만큼 제거
check = 0
i = len(s) - 1
while check < n // 2 and i >= 0:
    if s[i] == '0':
        s.pop(i)
        check += 1
        # pop()으로 요소를 제거하면 리스트가 뒤로 당겨지므로 i를 감소시키지 않음
    i -= 1  # '0'이 아닌 경우에도 인덱스를 감소하여 뒤에서부터 탐색

# 최종 결과 출력
print("".join(s))
