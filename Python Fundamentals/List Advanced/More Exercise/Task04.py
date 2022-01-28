n = int(input())
field = []
destroyed_ship = 0
for number_row in range(n):
    row = [int(x) for x in input().split(" ")]
    field.append(row)

shoots = input().split(" ")

for shot in shoots:
    shot = shot.split("-")
    row = int(shot[0])
    col = int(shot[1])
    if field[row][col] != 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ship += 1

print(destroyed_ship)

