rows, columns = [int(num) for num in input().split()]

matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

match_count = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol_1 = matrix[row][column]
        symbol_2 = matrix[row][column + 1]
        symbol_3 = matrix[row + 1][column]
        symbol_4 = matrix[row + 1][column + 1]

        if symbol_1 == symbol_2 == symbol_3 == symbol_4:
            match_count += 1

print(match_count)
