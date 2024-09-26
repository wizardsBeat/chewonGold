# 백준 17413번 문제 풀이

str = input().strip()  # 문자열 입력
stack = []  # 뒤집을 문자열 담을 스택
tag = False  # 태그 내부인지 아닌지 판단
result = []  # 결과 담을 리스트

for s in str:
    # 태그 시작
    if s == "<":
        while stack:  # 스택에 있는 문자가 있다면 뒤집어 결과에 추가
            result.append(stack.pop())
        tag = True
        result.append(s)  # '<' 추가

    # 태그 끝
    elif s == ">":
        tag = False
        result.append(s)  # '>' 추가

    # 태그 내부일 경우 그대로 추가
    elif tag:
        result.append(s)

    # 공백을 만나면 스택에 있는 단어를 뒤집어서 결과에 추가
    elif s == " ":
        while stack:
            result.append(stack.pop())
        result.append(s)  # 공백 추가

    # 태그 외부의 단어를 스택에 추가
    else:
        stack.append(s)

# 마지막 남아 있는 스택 처리
while stack:
    result.append(stack.pop())

# 리스트를 문자열로 변환하여 출력
print(''.join(result))
