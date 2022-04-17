def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


player_one, player_two = [el for el in input().split(", ")]
n = 7
matrix = []
player_one_score = 501
player_two_score = 501
throws_counter = 0
player_one_won = False
player_two_won = False

for _ in range(n):
    data = [int(el) if el.isdigit() else el for el in input().split()]
    matrix.append(data)

while True:
    row, col = [int(el) for el in input()[1:-1].split(", ")]
    current_score = 0
    throws_counter += 1
    if is_valid(row, col, n):
        if matrix[row][col] == "D":
            current_score = (matrix[0][col] + matrix[n-1][col] + matrix[row][0] + matrix[row][n-1]) * 2
        elif matrix[row][col] == "T":
            current_score = (matrix[0][col] + matrix[n-1][col] + matrix[row][0] + matrix[row][n-1]) * 3
        elif matrix[row][col] == "B":
            if throws_counter % 2 != 0:
                player_one_won = True
            else:
                player_two_won = True
            break
        else:
            current_score = matrix[row][col]

        if throws_counter % 2 != 0:
            player_one_score -= current_score
            if player_one_score <= 0:
                player_one_won = True
                break
        else:
            player_two_score -= current_score
            if player_two_score <= 0:
                player_two_won = True
                break

if player_one_won:
    print(f"{player_one} won the game with {(throws_counter // 2) + 1} throws!")
if player_two_won:
    print(f"{player_two} won the game with {throws_counter // 2} throws!")

