def is_valid(start_row, start_column, size):
    if 0 <= start_row < size and 0 <= start_column < size:
        return True
    return False


n = int(input())
matrix = [[int(num) for num in input().split(", ")] for _ in range(n)]

primary_sum = 0
primary_diagonals = []
primary_start_row = 0
primary_start_column = 0
primary_move_down_right = (1, 1)

while is_valid(primary_start_row, primary_start_column, n):
    primary_sum += matrix[primary_start_row][primary_start_column]
    primary_diagonals.append(matrix[primary_start_row][primary_start_column])
    primary_start_row += primary_move_down_right[0]
    primary_start_column += primary_move_down_right[1]

secondary_sum = 0
secondary_diagonals = []
secondary_start_row = 0
secondary_start_column = n - 1
secondary_move_down_left = (1, -1)

while is_valid(secondary_start_row, secondary_start_column, n):
    secondary_sum += matrix[secondary_start_row][secondary_start_column]
    secondary_diagonals.append(matrix[secondary_start_row][secondary_start_column])
    secondary_start_row += secondary_move_down_left[0]
    secondary_start_column += secondary_move_down_left[1]

print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonals])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonals])}. Sum: {secondary_sum}")

