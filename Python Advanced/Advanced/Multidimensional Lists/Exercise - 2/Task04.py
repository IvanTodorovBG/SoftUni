def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    data = [int(el) if el not in ("X", "B") else el for el in input().split()]
    matrix.append(data)

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

bunny_row = int
bunny_col = int
max_direction = ""
max_positions = []
max_eggs = float('-inf')

for row in range(n):
    for column in range(n):
        if matrix[row][column] == "B":
            bunny_row = row
            bunny_col = column

for direction in all_directions:
    next_row = bunny_row + all_directions[direction][0]
    next_column = bunny_col + all_directions[direction][1]

    current_eggs = 0
    current_positions = []
    while is_valid(next_row, next_column, n):
        if matrix[next_row][next_column] == "X":
            break
        else:
            current_eggs += matrix[next_row][next_column]
            current_positions.append([next_row, next_column])

            next_row += all_directions[direction][0]
            next_column += all_directions[direction][1]

    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        max_direction = direction
        max_positions = current_positions

print(max_direction)
for sublist in max_positions:
    print(sublist)
print(max_eggs)
