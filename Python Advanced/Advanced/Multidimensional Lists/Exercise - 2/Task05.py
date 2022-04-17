def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    data = [int(el) if el not in ("A", "R", ".") else el for el in input().split()]
    matrix.append(data)

alice_row = int
alice_col = int

for row in range(n):
    for column in range(n):
        if matrix[row][column] == "A":
            alice_row = row
            alice_col = column
            matrix[alice_row][alice_col] = "*"

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0

while True:
    command = input()

    next_row = alice_row + all_directions[command][0]
    next_col = alice_col + all_directions[command][1]
    if is_valid(next_row, next_col, n):
        if matrix[next_row][next_col] == "R":
            matrix[next_row][next_col] = "*"
            break

        elif type(matrix[next_row][next_col]) == int:
            tea_bags += matrix[next_row][next_col]

        alice_row = next_row
        alice_col = next_col
        matrix[alice_row][alice_col] = "*"

        if tea_bags >= 10:
            break
    else:
        break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for sublist in matrix:
    print(' '.join([str(x) for x in sublist]))
