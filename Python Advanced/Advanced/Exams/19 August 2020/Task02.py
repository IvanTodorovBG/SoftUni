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

n = int(input())
bombs = int(input())
matrix = []

for _ in range(n):
    data = list("0" * n)
    matrix.append(data)

for current_bomb in range(bombs):

    row, col = [int(el) for el in input()[1:-1].split(", ")]

    matrix[row][col] = "*"

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "*":
            for direction in all_directions:
                next_row = row + all_directions[direction][0]
                next_col = col + all_directions[direction][1]
                if is_valid(next_row, next_col, n):
                    if matrix[next_row][next_col] == "0":
                        matrix[next_row][next_col] = 1
                    elif type(matrix[next_row][next_col]) == int:
                        matrix[next_row][next_col] += 1

for sublist in matrix:
    print(" ".join([str(x) for x in sublist]))
