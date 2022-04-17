def is_valid(next_r, next_c):
    if 0 <= next_r < 8 and 0 <= next_c < 8:
        return True
    return False


matrix = []
queens = []

for _ in range(8):
    matrix.append(input().split(" "))

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

for row in range(8):
    for column in range(8):
        if matrix[row][column] == "Q":
            row_q = row
            col_q = column
            for rotation in rotations:
                next_row = row_q + rotations[rotation][0]
                next_col = col_q + rotations[rotation][1]
                while is_valid(next_row, next_col):
                    if matrix[next_row][next_col] == "K":
                        queens.append([row_q, col_q])
                        break
                    elif matrix[next_row][next_col] == "Q":
                        break
                    else:
                        next_row += rotations[rotation][0]
                        next_col += rotations[rotation][1]

if queens:
    [print(q) for q in queens]
else:
    print("The king is safe!")
