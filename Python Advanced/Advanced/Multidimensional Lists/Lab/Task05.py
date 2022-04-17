def is_valid(current_row, current_column, size):
    if 0 <= current_row < size and 0 <= current_column < size:
        return True
    return False


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
sum_diagonal = 0

down_right = (1, 1)
start_row = 0
start_column = 0

while True:

    if is_valid(start_row, start_column, n):
        sum_diagonal += matrix[start_row][start_column]
        start_row += down_right[0]
        start_column += down_right[1]

    else:
        break

print(sum_diagonal)