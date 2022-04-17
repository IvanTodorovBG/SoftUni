def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


count_presents = int(input())
n = int(input())

matrix = []
nice_kids_count = 0
given_to_nice = 0

for _ in range(n):
    data = input().split()
    matrix.append(data)
    nice_kids_count += data.count("V")

santa_row = int
santa_col = int

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col

all_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:

    command = input()

    if command == "Christmas morning":
        break

    next_row = santa_row + all_directions[command][0]
    next_col = santa_col + all_directions[command][1]

    if is_valid(next_row, next_col, n):

        if matrix[next_row][next_col] == "V":
            given_to_nice += 1
            count_presents -= 1

        elif matrix[next_row][next_col] == "C":
            for direction in all_directions:
                next_step_row = next_row + all_directions[direction][0]
                next_step_col = next_col + all_directions[direction][1]
                if is_valid(next_step_row, next_step_col, n):
                    if matrix[next_step_row][next_step_col] == "V":
                        given_to_nice += 1
                        count_presents -= 1
                    elif matrix[next_step_row][next_step_col] == "X":
                        count_presents -= 1
                    matrix[next_step_row][next_step_col] = "-"
                    if count_presents == 0:
                        break

        matrix[santa_row][santa_col] = "-"
        matrix[next_row][next_col] = "S"
        santa_row = next_row
        santa_col = next_col

        if count_presents == 0:
            break

if count_presents == 0 and nice_kids_count != given_to_nice:
    print("Santa ran out of presents!")

for sublist in matrix:
    print(" ".join(sublist))

if nice_kids_count == given_to_nice:
    print(f"Good job, Santa! {given_to_nice} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count - given_to_nice} nice kid/s.")