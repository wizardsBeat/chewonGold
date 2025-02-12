# 후위 표기식2
num_list = []
# 피연산자의 개수
N = int(input())
# 후위표기식
calc = list(input())
for i in range(N):
    num = float(input())
    num_list.append(num)
    
# 알파벳(A, B, C...)과 숫자를 매핑
operand_dict = {chr(65 + i): num_list[i] for i in range(N)}
def calculator(n1, n2, s):
    if s == '+':
        sum = n1 + n2
    if s == '-':
        sum = n1 - n2
    if s == '*':
        sum = n1 * n2
    if s == '/':
        sum = n1 / n2
    return sum
stack = []
for c in calc:
    if c in operand_dict:  # 피연산자이면 숫자로 변환해서 스택에 push
        stack.append(operand_dict[c])
    else:  # 연산자이면 스택에서 두 개의 피연산자를 꺼내서 계산 후 push
        n2 = stack.pop()
        n1 = stack.pop()
        result = calculator(n1, n2, c)
        stack.append(result)
# 최종 결과 출력
print(f"{stack[-1]:.2f}")