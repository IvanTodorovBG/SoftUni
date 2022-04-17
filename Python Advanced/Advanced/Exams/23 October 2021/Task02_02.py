def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = 6
matrix = []
total_score = 0
prize = ""
for _ in range(n):
    line = [int(el) if el.isdigit() else el for el in input().split(" ")]
    matrix.append(line)

for current_throw in range(3):
    row, col = [int(el) for el in input()[1:-1].split(", ")]

    if is_valid(row, col, n):
        if matrix[row][col] == "B":
            matrix[row][col] = 0
            for index in range(n):
                total_score += matrix[index][col]

if 100 <= total_score <= 199:
    prize = "Football"
elif 200 <= total_score <= 299:
    prize = "Teddy Bear"
elif total_score >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {total_score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_score} points more to win a prize.")




