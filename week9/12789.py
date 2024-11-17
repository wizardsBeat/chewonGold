def dokidoki_snack_delivery():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    students = list(map(int, data[1:]))
    
    stack = []
    current = 1  # 간식을 나눠줄 순번
    
    for student in students:
        while stack and stack[-1] == current:
            stack.pop()
            current += 1
        if student == current:
            current += 1
        else:
            stack.append(student)
    
    # 남아있는 스택을 확인
    while stack:
        if stack.pop() == current:
            current += 1
        else:
            print("Sad")
            return
    
    print("Nice")


dokidoki_snack_delivery()
