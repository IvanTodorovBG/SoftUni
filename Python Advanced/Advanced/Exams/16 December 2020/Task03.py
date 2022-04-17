def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    # creating the matrix
    for index in range(3, n + 1):
        line = [0] * index
        line[0] = 1
        line[-1] = 1
        matrix.append(line)

    # filling up the matrix
    for row in range(n):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                matrix[row][col] = matrix[row - 1][col] + matrix[row - 1][col - 1]
    return matrix
