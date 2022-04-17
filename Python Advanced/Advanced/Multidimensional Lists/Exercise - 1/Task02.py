def is_valid(row, column, size):
    if 0 <= row < size and 0 <= column < size:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    line = [int(num) for num in input().split()]
    matrix.append(line)

primary_sum = 0
primary_row = 0
primary_column = 0
primary_move_down_right = (1, 1)

while is_valid(primary_row, primary_column, n):
    primary_sum += matrix[primary_row][primary_column]
    primary_row += primary_move_down_right[0]
    primary_column += primary_move_down_right[1]

secondary_sum = 0
secondary_row = 0
secondary_column = n - 1
secondary_move_down_left = (1, -1)

while is_valid(secondary_row, secondary_column, n):
    secondary_sum += matrix[secondary_row][secondary_column]
    secondary_row += secondary_move_down_left[0]
    secondary_column += secondary_move_down_left[1]

diagonal_diff = abs(primary_sum - secondary_sum)

print(diagonal_diff)
