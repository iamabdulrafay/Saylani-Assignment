matrix_1 = [
    [1, 2, 5],
    [2, 4, 3],
    [1, 2, 1],
]

matrix_2 = [
    [1, 2, 3],
    [5, 4, 6],
    [1, 5, 3],
]

result = []

for row in range(len(matrix_1)):
    result_row = []
    for col in range(len(matrix_1[row])):
        result_row.append(matrix_1[row][col] + matrix_2[row][col])
    result.append(result_row)

# Printing the result
for row in result:
    print(row)

# Assignment 4 Question No. 10
matrix_1 = [
    [1, 2, 5],
    [2, 4, 3],
    [1, 2, 1],
]

matrix_2 = [
    [1, 2, 3],
    [5, 4, 6],
    [1, 5, 3],
]

result = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[i])):
        sum_value = matrix_1[i][j] + matrix_2[i][j]
        row.append(sum_value)
    result.append(row)

print(result)
