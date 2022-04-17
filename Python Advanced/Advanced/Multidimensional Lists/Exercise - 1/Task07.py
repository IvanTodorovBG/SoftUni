from collections import deque
rows, columns = [int(num) for num in input().split()]
matrix = []
snake_move = deque(input())

for row in range(rows):
    line = []
    if row % 2 == 0:
        for column in range(columns):
            line.append(snake_move[0])
            snake_move.append(snake_move.popleft())
        matrix.append(line)
    else:
        for column in range(columns):
            line.append(snake_move[0])
            snake_move.append(snake_move.popleft())
        matrix.append(line[::-1])

for sublist in matrix:
    print("".join(sublist))
