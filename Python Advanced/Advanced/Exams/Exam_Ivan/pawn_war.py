def is_valid(current_row, current_col, size):
    if 0 <= current_row < size and 0 <= current_col < size:
        return True
    return False


def do_chessboard(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def find_player_positions(matrix, size):
    white_r = int
    white_c = int
    black_r = int
    black_c = int
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "w":
                white_r, white_c = r, c
            elif matrix[r][c] == "b":
                black_r, black_c = r, c
    return white_r, white_c, black_r, black_c


def do_nums_and_letters(size):
    nums = {}
    letts = {}
    for i in range(size):
        nums[i] = str(8 - i)
        letts[i] = chr(97 + i)
    return nums, letts


n = 8

game_over = False

chessboard = do_chessboard(n)
numbers, letters = do_nums_and_letters(n)

white_row, white_col, black_row, black_col = find_player_positions(chessboard, n)

white_diagonals = {
        "up_left": (-1, -1),
        "up_right": (-1, 1)}

black_diagonals = {
        "down_left": (1, -1),
        "down_right": (1, 1)}

player_turn = 1
while True:
    player_turn = 2 if player_turn % 2 == 0 else 1

    # white player
    if player_turn == 1:
        for diagonal in white_diagonals:
            next_row = white_row + white_diagonals[diagonal][0]
            next_col = white_col + white_diagonals[diagonal][1]
            if is_valid(next_row, next_col, n):
                if chessboard[next_row][next_col] == 'b':
                    print(f"Game over! White win, capture on {letters[next_col] + numbers[next_row]}.")
                    game_over = True
                    break
        if game_over:
            break

        chessboard[white_row][white_col] = '-'
        white_row -= 1
        chessboard[white_row][white_col] = 'w'

        if white_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {letters[white_col] + numbers[white_row]}.")
            break

    # black player
    elif player_turn == 2:
        for diagonal in black_diagonals:
            next_row = black_row + black_diagonals[diagonal][0]
            next_col = black_col + black_diagonals[diagonal][1]
            if is_valid(next_row, next_col, n):
                if chessboard[next_row][next_col] == 'w':
                    print(f"Game over! Black win, capture on {letters[next_col] + numbers[next_row]}.")
                    game_over = True
                    break
        if game_over:
            break

        chessboard[black_row][black_col] = '-'
        black_row += 1
        chessboard[black_row][black_col] = 'b'

        if black_row == n - 1:
            print(f"Game over! Black pawn is promoted to a queen at {letters[black_col] + numbers[black_row]}.")
            break

    player_turn += 1