def is_valid(row, column, size):
    if 0 <= row < size and 0 <= column < size:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    line = [int(num) for num in input().split()]
    matrix.append(line)

command = input()

while command != "END":
    command = command.split()
    order = command[0]
    given_row = int(command[1])
    given_column = int(command[2])
    given_value = int(command[3])

    if order == "Add":
        if is_valid(given_row, given_column, n):
            matrix[given_row][given_column] += given_value
        else:
            print("Invalid coordinates")

    elif order == "Subtract":
        if is_valid(given_row, given_column, n):
            matrix[given_row][given_column] -= given_value
        else:
            print("Invalid coordinates")

    command = input()

for sublist in matrix:
    for num in sublist:
        print(''.join(str(num)), end=" ")
    print()
