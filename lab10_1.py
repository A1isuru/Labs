def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + j >= n -1: 
                matrix[i][j] = j - (n - 1) + n - i

    return matrix

while True:
    n = input("Введите натуральное число N: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")
        
matrix = create_matrix(n)
for row in matrix:
    print(row)