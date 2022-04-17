def is_valid(current_row, current_col, size):
    if 0 <= current_row < size and 0 <= current_col < size:
        return True
    return False


n = 8

matrix = []

w_row = int
w_col = int
b_row = int
b_col = int

game_over = False

for _ in range(8):
    matrix.append(input().split())

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "w":
            w_row, w_col = row, col
        elif matrix[row][col] == "b":
            b_row, b_col = row, col

up_white = (-1, 0)
down_black = (1, 0)

white_diagonals = {
    "up_left": (-1, -1),
    "up_right": (-1, 1),
}

black_diagonals = {
    "down_left": (1, -1),
    "down_right": (1, 1)
}

nums = {}
letters = {}
for key in range(8):
    nums[key] = str(8 - key)
    letters[key] = chr(97 + key)

turns = 0
while True:
    turns += 1

    # white player
    if turns % 2 != 0:
        for diagonal in white_diagonals:
            next_row = w_row + white_diagonals[diagonal][0]
            next_col = w_col + white_diagonals[diagonal][1]
            if is_valid(next_row, next_col, n):
                if next_row == b_row and next_col == b_col:
                    print(f"Game over! White win, capture on {letters[next_col] + nums[next_row]}.")
                    game_over = True
                    break
        if game_over:
            break

        w_row += up_white[0]
        w_col += up_white[1]

        if w_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {letters[w_col] + nums[w_row]}.")
            break

    # black player
    else:
        for diagonal in black_diagonals:
            next_row = b_row + black_diagonals[diagonal][0]
            next_col = b_col + black_diagonals[diagonal][1]
            if is_valid(next_row, next_col, n):
                if next_row == w_row and next_col == w_col:
                    print(f"Game over! Black win, capture on {letters[next_col] + nums[next_row]}.")
                    game_over = True
                    break
        if game_over:
            break

        b_row += down_black[0]
        b_col += down_black[1]

        if b_row == 7:
            print(f"Game over! Black pawn is promoted to a queen at {letters[b_col] + nums[b_row]}.")
            break