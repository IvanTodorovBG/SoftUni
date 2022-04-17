def is_valid(row_ahead, column_ahead, n_rows, n_columns):
    if 0 <= row_ahead < n_rows and 0 <= column_ahead < n_columns:
        return True
    return False


count_rows, count_columns = [int(x) for x in input().split()]

matrix = []

for _ in range(count_rows):
    data = input().split()
    matrix.append(data)

matches = 0

for row in range(count_rows - 1):
    for column in range(count_columns - 1):
        if is_valid(row + 1, column + 1, count_rows, count_columns):
            symbol_1 = matrix[row][column]
            symbol_2 = matrix[row][column + 1]
            symbol_3 = matrix[row + 1][column]
            symbol_4 = matrix[row + 1][column + 1]
            if symbol_1 == symbol_2 == symbol_3 == symbol_4:
                matches += 1

print(matches)
