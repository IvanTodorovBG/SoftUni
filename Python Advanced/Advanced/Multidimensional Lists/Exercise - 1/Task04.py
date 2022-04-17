rows, columns = [int(num) for num in input().split()]
matrix = []

for _ in range(rows):
    line = [int(num) for num in input().split()]
    matrix.append(line)

max_num_1 = 0
max_num_2 = 0
max_num_3 = 0
max_num_4 = 0
max_num_5 = 0
max_num_6 = 0
max_num_7 = 0
max_num_8 = 0
max_num_9 = 0
max_sum = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        num_1 = matrix[row][column]
        num_2 = matrix[row][column + 1]
        num_3 = matrix[row][column + 2]
        num_4 = matrix[row + 1][column]
        num_5 = matrix[row + 1][column + 1]
        num_6 = matrix[row + 1][column + 2]
        num_7 = matrix[row + 2][column]
        num_8 = matrix[row + 2][column + 1]
        num_9 = matrix[row + 2][column + 2]
        current_sum = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9

        if current_sum > max_sum:
            max_sum = current_sum
            max_num_1 = num_1
            max_num_2 = num_2
            max_num_3 = num_3
            max_num_4 = num_4
            max_num_5 = num_5
            max_num_6 = num_6
            max_num_7 = num_7
            max_num_8 = num_8
            max_num_9 = num_9

print(f"Sum = {max_sum}")
print(f"{max_num_1} {max_num_2} {max_num_3}")
print(f"{max_num_4} {max_num_5} {max_num_6}")
print(f"{max_num_7} {max_num_8} {max_num_9}")