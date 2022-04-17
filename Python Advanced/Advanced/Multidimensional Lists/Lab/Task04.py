rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(i) for i in input().split()] for _ in range(rows)]

for column in range(columns):
    sum_column = 0
    for row in range(rows):
        sum_column += matrix[row][column]
    print(sum_column)
