def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

all_directions = {
    1: (-2, -1),
    2: (-2, 1),
    3: (-1, 2),
    4: (1, 2),
    5: (2, 1),
    6: (2, -1),
    7: (1, -2),
    8: (-1, -2)
}

removed_knights = 0

while True:

    max_hits = 0
    max_row = int
    max_column = int

    for row in range(n):
        for column in range(n):
            if matrix[row][column] == "K":
                current_hits = 0
                for direction in all_directions:
                    next_row = row + all_directions[direction][0]
                    next_column = column + all_directions[direction][1]
                    if is_valid(next_row, next_column, n):
                        if matrix[next_row][next_column] == "K":
                            current_hits += 1
                if current_hits > max_hits:
                    max_hits = current_hits
                    max_row = row
                    max_column = column

    if max_hits == 0:
        break

    removed_knights += 1
    matrix[max_row][max_column] = "0"

print(removed_knights)
