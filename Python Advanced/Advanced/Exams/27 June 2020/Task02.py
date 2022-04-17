def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
matrix = []
hole_addresses = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

food_quantity = 0
snake_row = int
snake_col = int

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "B":
            hole_addresses.append([row, col])
        elif matrix[row][col] == "S":
            snake_row = row
            snake_col = col

while True:

    direction = input()

    next_row = snake_row + all_directions[direction][0]
    next_col = snake_col + all_directions[direction][1]

    if is_valid(next_row, next_col, n):
        if matrix[next_row][next_col] == "-":
            matrix[snake_row][snake_col] = "."
            matrix[next_row][next_col] = "S"
            snake_row = next_row
            snake_col = next_col

        elif matrix[next_row][next_col] == "*":
            matrix[snake_row][snake_col] = "."
            matrix[next_row][next_col] = "S"
            snake_row = next_row
            snake_col = next_col
            food_quantity += 1
            if food_quantity == 10:
                break

        elif matrix[next_row][next_col] == "B":
            matrix[snake_row][snake_col] = "."
            matrix[next_row][next_col] = "."
            go_out = None
            address = [next_row, next_col]
            for adr in hole_addresses:
                if adr != address:
                    go_out = adr
            next_step_row, next_step_col = go_out
            matrix[next_step_row][next_step_col] = "S"
            snake_row = next_step_row
            snake_col = next_step_col
    else:
        matrix[snake_row][snake_col] = "."
        break

if food_quantity == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity}")

for sublist in matrix:
    print("".join(sublist))