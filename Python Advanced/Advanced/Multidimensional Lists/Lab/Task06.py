n = int(input())
matrix = [[x for x in input()] for _ in range(n)]
symbol = input()
location = ()
found = False

for row in range(n):
    if found:
        break
    for column in range(n):
        if matrix[row][column] == symbol:
            location = (row, column)
            found = True
            break

if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")



