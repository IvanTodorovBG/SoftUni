def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())
movements = input().split()
matrix = []
total_coals = 0
collected_coal = 0
game_over = False

for _ in range(n):
    data = input().split()
    matrix.append(data)
    total_coals += data.count("c")

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

miner_row = int
miner_col = int

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            miner_row = row
            miner_col = col

for current_move in movements:
    next_row = miner_row + all_directions[current_move][0]
    next_col = miner_col + all_directions[current_move][1]
    if is_valid(next_row, next_col, n):
        miner_row = next_row
        miner_col = next_col

        if matrix[next_row][next_col] == "e":
            game_over = True
            break

        elif matrix[next_row][next_col] == "c":
            matrix[next_row][next_col] = "*"
            collected_coal += 1

        if collected_coal == total_coals:
            break

if collected_coal == total_coals:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif game_over:
    print(f"Game over! ({miner_row}, {miner_col})")
else:
    print(f"{total_coals - collected_coal} pieces of coal left. ({miner_row}, {miner_col})")
