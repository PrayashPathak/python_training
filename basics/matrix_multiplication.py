matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3], [1, 2, 3], [3, 4, 5]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
            result[i][j] += matrix_a[i][j] * matrix_b[i][j]
print(result)
