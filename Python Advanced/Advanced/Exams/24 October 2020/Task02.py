def is_valid_row_col(next_r, next_c):
    if 0 <= next_r < 8 and 0 <= next_c < 8:
        return True
    return False


matrix = []
queens = []

for _ in range(8):
    data = input().split(" ")
    matrix.append(data)

row_king = int
col_king = int

for row in range(8):
    for column in range(8):
        if matrix[row][column] == "K":
            row_king = row
            col_king = column

rotations = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

for rotation in rotations:
    next_row = row_king + rotations[rotation][0]
    next_col = col_king + rotations[rotation][1]

    while is_valid_row_col(next_row, next_col):
        if matrix[next_row][next_col] == "Q":
            queens.append([next_row, next_col])
            break
        next_row += rotations[rotation][0]
        next_col += rotations[rotation][1]

if queens:
    [print(q) for q in queens]
else:
    print("The king is safe!")
