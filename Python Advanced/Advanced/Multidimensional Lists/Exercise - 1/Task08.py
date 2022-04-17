def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

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

all_bombs = list(input().split())

for current_bomb in all_bombs:
    bomb_coordinates = current_bomb.split(",")
    bomb_row = int(bomb_coordinates[0])
    bomb_col = int(bomb_coordinates[1])

    if is_valid(bomb_row, bomb_col, n):
        bomb = matrix[bomb_row][bomb_col]
        if bomb > 0:
            matrix[bomb_row][bomb_col] = 0
            for direction in all_directions:
                next_row = bomb_row + all_directions[direction][0]
                next_col = bomb_col + all_directions[direction][1]
                if is_valid(next_row, next_col, n):
                    if matrix[next_row][next_col] > 0:
                        matrix[next_row][next_col] -= bomb
active_cells = []
for sublist in matrix:
    for num in sublist:
        if num > 0:
            active_cells.append(num)

print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")
for sublist in matrix:
    print(" ".join(str(el) for el in sublist))