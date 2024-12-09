import sys

n = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [0, 0, 0]

def count_picture(matrix):
    global count
    size = len(matrix)
    flag = 0
    first = matrix[0][0]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != first:
                flag = 1
                break
    if flag == 1:
        new_size = size // 3
        for i in range(3):
            row_start = i*new_size
            row_end = row_start + new_size
            for j in range(3):
                column_start = j*new_size
                column_end = column_start + new_size
                new_matrix = []
                for row in matrix[row_start:row_end]:
                    new_row = row[column_start:column_end]
                    new_matrix.append(new_row)

                count_picture(new_matrix)
    else:
        if matrix[0][0] == -1:
            count[0] += 1
        elif matrix[0][0] == 0:
            count[1] += 1
        else:
            count[2] += 1
        return
    
count_picture(matrix)
print('\n'.join(map(str, count)))