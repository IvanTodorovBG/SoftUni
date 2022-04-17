def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


word = list(input())
n = int(input())
matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

player_row = int
player_col = int

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col

m = int(input())

for _ in range(m):

    direction = input()

    next_row = player_row + all_directions[direction][0]
    next_col = player_col + all_directions[direction][1]

    if is_valid(next_row, next_col, n):
        matrix[player_row][player_col] = "-"
        if matrix[next_row][next_col] != "-":
            word.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = "P"
        player_row = next_row
        player_col = next_col

    else:
        if word:
            word.pop()

print("".join(word))
for sublist in matrix:
    print("".join(sublist))

