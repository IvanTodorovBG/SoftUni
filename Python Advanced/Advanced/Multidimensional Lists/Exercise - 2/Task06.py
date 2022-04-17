def all_directions_shooting(direct, r, c):
    if direct == "right":
        return r, c + 1
    elif direct == "left":
        return r, c - 1
    elif direct == "up":
        return r - 1, c
    elif direct == "down":
        return r + 1, c


def all_directions_movement(movement, ahead_row, ahead_col, current_steps):
    if movement == "right":
        return ahead_row, ahead_col + current_steps
    elif movement == "left":
        return ahead_row, ahead_col - current_steps
    elif movement == "up":
        return ahead_row - current_steps, ahead_col
    elif movement == "down":
        return ahead_row + current_steps, ahead_col


def is_valid(ahead_r, ahead_c, size):
    if 0 <= ahead_r < size and 0 <= ahead_c < size:
        return True
    return False


n = 5

matrix = []
targets_positions = []
total_targets = 0
won = False

for _ in range(n):
    data = input().split()
    matrix.append(data)
    total_targets += data.count("x")

player_row = int
player_col = int
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "A":
            player_row = row
            player_col = col

number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    order = command[0]
    direction = command[1]

    if order == "shoot":

        next_row, next_col = all_directions_shooting(direction, player_row, player_col)

        while is_valid(next_row, next_col, n):
            if matrix[next_row][next_col] == "x":
                targets_positions.append([next_row, next_col])
                matrix[next_row][next_col] = "."
                break
            else:
                next_row, next_col = all_directions_shooting(direction, next_row, next_col)

        if len(targets_positions) == total_targets:
            won = True
            break

    elif order == "move":
        steps = int(command[2])
        next_row, next_col = all_directions_movement(direction, player_row, player_col, steps)
        if is_valid(next_row, next_col, n) and matrix[next_row][next_col] == ".":
            matrix[player_row][player_col] = "."
            matrix[next_row][next_col] = "A"
            player_row = next_row
            player_col = next_col

remaining_targets = total_targets - len(targets_positions)

if remaining_targets:
    print(f"Training not completed! {remaining_targets} targets left.")
else:
    print(f"Training completed! All {total_targets} targets hit.")

for sub in targets_positions:
    print(sub)
