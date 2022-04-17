def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

n = 8
matrix = []
queens = []

for _ in range(n):
    data = input().split()
    matrix.append(data)

king_row = int
king_col = int

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "K":
            king_row = row
            king_col = col

for direction in all_directions:

    next_row = king_row + all_directions[direction][0]
    next_col = king_col + all_directions[direction][1]

    while is_valid(next_row, next_col, n):
        if matrix[next_row][next_col] == "Q":
            queens.append([next_row, next_col])
            break
        next_row += all_directions[direction][0]
        next_col += all_directions[direction][1]

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")