def is_not_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return False
    return True


all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
matrix = []

for _ in range(n):
    data = [int(el) if el.isdigit() else el for el in input().split()]
    matrix.append(data)

total_coins = 0
player_row = int
player_col = int
player_path = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
            player_path.append([player_row, player_col])
            matrix[player_row][player_col] = 0

while True:

    direction = input()

    if direction not in all_directions:
        continue

    next_row = player_row + all_directions[direction][0]
    next_col = player_col + all_directions[direction][1]

    if is_not_valid(next_row, next_col, n):

        if direction == "up":
            next_row = n - 1
        elif direction == "down":
            next_row = 0
        elif direction == "left":
            next_col = n - 1
        elif direction == "right":
            next_col = 0

    if matrix[next_row][next_col] == "X":
        total_coins = int(total_coins * 0.5)
        player_path.append([next_row, next_col])
        break
    else:
        total_coins += matrix[next_row][next_col]
        matrix[next_row][next_col] = 0
        player_row = next_row
        player_col = next_col
        player_path.append([player_row, player_col])
        if total_coins >= 100:
            break

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print("Your path:")
for sublist in player_path:
    print(sublist)
