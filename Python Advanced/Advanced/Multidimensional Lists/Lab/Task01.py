rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)
    total_sum += sum(lines)

print(total_sum)
print(matrix)
