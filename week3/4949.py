import sys

def balance(sentence):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'} #열고 닫는 괄호 쌍을 딕셔너리로 지정
    
    for s in sentence:
        if s in matching.values(): # 만약 여는 괄호라면 스택에 괄호 저장
            stack.append(s)
        elif s in matching.keys():  #만약 닫는 괄호라면
            if not stack or stack[-1] != matching[s]: # 스택이 비어있지 않거나 맞는 괄호가 아니라면 False 리턴
                return False
            stack.pop() #스택에서 제거해주기
    return len(stack) == 0 

        
answer = []

while True:
    lines = str(sys.stdin.readline().rstrip()) #input의 개행 문자만 제거해주기 위해 rstrip사용
    if lines == ".":
        break
    if balance(lines):
        answer.append("yes")
    elif balance(lines) == False:
        answer.append("no")
    
print("\n".join(map(str, answer)))
