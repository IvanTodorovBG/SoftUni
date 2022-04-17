def is_valid(current_row, current_column, row_ahead, column_ahead, n_rows, n_columns):
    if 0 <= current_row < n_rows and 0 <= current_column < n_columns and \
            0 <= row_ahead < n_rows and 0 <= column_ahead < n_columns:
        return True
    return False


count_rows, count_columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(count_rows)]
max_sum = 0
row_one = None
row_two = None

for row in range(count_rows):
    for column in range(count_columns):

        if is_valid(row, column, row + 1, column + 1, count_rows, count_columns):
            number = matrix[row][column]
            number_2 = matrix[row][column + 1]
            number_3 = matrix[row + 1][column]
            number_4 = matrix[row + 1][column + 1]
            sum = number + number_2 + number_3 + number_4
            if sum > max_sum:
                max_sum = sum
                row_one = [number, number_2]
                row_two = [number_3, number_4]

print(" ".join([str(x) for x in row_one]))
print(" ".join([str(x) for x in row_two]))
print(max_sum)