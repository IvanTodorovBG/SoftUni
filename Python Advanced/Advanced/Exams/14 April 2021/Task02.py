def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


player_one, player_two = input().split(", ")
n = 7
matrix = []
counter = 0
player_one_score = 501
player_two_score = 501
player_one_win = False
player_two_win = False

for _ in range(n):
    line = [int(num) if num.isdigit() else num for num in input().split()]
    matrix.append(line)

while True:
    row, col = [int(num) for num in input()[1:-1].split(", ")]
    counter += 1
    if is_valid(row, col, n):
        if type(matrix[row][col]) == int:
            if counter % 2 != 0:
                player_one_score -= matrix[row][col]
            else:
                player_two_score -= matrix[row][col]

        elif matrix[row][col] == "D":
            if counter % 2 != 0:
                player_one_score -= (matrix[0][col] + matrix[-1][col] + matrix[row][0] + matrix[row][-1]) * 2
            else:
                player_two_score -= (matrix[0][col] + matrix[-1][col] + matrix[row][0] + matrix[row][-1]) * 2

        elif matrix[row][col] == "T":
            if counter % 2 != 0:
                player_one_score -= (matrix[0][col] + matrix[-1][col] + matrix[row][0] + matrix[row][-1]) * 3
            else:
                player_two_score -= (matrix[0][col] + matrix[-1][col] + matrix[row][0] + matrix[row][-1]) * 3

        elif matrix[row][col] == "B":
            if counter % 2 != 0:
                player_one_win = True
                break
            else:
                player_two_win = True
                break

        if player_one_score <= 0:
            player_one_win = True
            break
        elif player_two_score <= 0:
            player_two_win = True
            break

if player_one_win:
    print(f"{player_one} won the game with {(counter // 2) + 1} throws!")
if player_two_win:
    print(f"{player_two} won the game with {counter // 2} throws!")
