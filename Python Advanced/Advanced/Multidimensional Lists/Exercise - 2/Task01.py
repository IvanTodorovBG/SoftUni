matrix = []

rows = input().split("|")

for row in rows:
    matrix.append(row.split())

for sublist in matrix[::-1]:
    for number in sublist:
        print(number, end=" ")

