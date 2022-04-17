def is_not_valid(r_1, c_1, r_2, c_2, total_rows, total_columns):
    if 0 <= r_1 < total_rows and 0 <= c_1 < total_columns and \
         0 <= r_2 < total_rows and 0 <= c_2 < total_columns:
        return False
    return True


rows, columns = [int(num) for num in input().split()]

matrix = []

for _ in range(rows):
    line = [int(num) for num in input().split()]
    matrix.append(line)

while True:
    command = input()

    if command == "END":
        break

    command = command.split()

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row_1 = int(command[1])
    col_1 = int(command[2])
    row_2 = int(command[3])
    col_2 = int(command[4])

    if is_not_valid(row_1, col_1, row_2, col_2, rows, columns):
        print("Invalid input!")
        continue

    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

    for row in range(rows):
        for column in range(columns):
            print(matrix[row][column], end=" ")
        print()

