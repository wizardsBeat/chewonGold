import sys
input = sys.stdin.readline

char = input()
m = int(input())

commands = []
for _ in range(m):
    commands.append(input())
    
loc = len(char)
char_list = list(char)

for command in commands:
    if command[0] == 'L':
        if loc > 0: loc -= 1
    elif command[0] == 'D':
        if loc < len(char): loc += 1
    elif command[0] == 'B':
        if loc > 0:
            loc -= 1
            del char_list[loc]
    elif command[0] == 'P':
        char_list.insert(loc, command.split()[1])
        loc += 1
        
print(*char_list, sep="")