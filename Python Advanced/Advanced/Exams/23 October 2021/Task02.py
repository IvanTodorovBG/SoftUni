import re


def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = 6
matrix = []

for _ in range(n):
    data = [int(el) if el.isdigit() else el for el in input().split()]
    matrix.append(data)

total_score = 0

for _ in range(3):

    coordinates = input()
    pattern = r"(\d+), (\d+)"

    for match in re.finditer(pattern, coordinates):
        row = int(match.group(1))
        col = int(match.group(2))

        if is_valid(row, col, n):
            if matrix[row][col] == "B":
                matrix[row][col] = 0
                for current_row in range(n):
                    if type(matrix[current_row][col]) == int:
                        total_score += matrix[current_row][col]

prize = ""

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

