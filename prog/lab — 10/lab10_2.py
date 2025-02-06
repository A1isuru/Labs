import random

def is_trace_of_square_of_symmetric_matrix(n):
    def generate_symmetric_matrix(size):
        matrix = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(i, size):
                value = random.randint(-10, 10)
                matrix[i][j] = value
                matrix[j][i] = value
        return matrix

    def matrix_multiply(A, B):
        size = len(A)
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def trace_of_matrix(A):
        return sum(A[i][i] for i in range(len(A)))
    
    for _ in range(1000):
        A = generate_symmetric_matrix(n)
        A_squared = matrix_multiply(A, A)
        trace = trace_of_matrix(A_squared)
        
        if trace == n:
            return True
    
    return False


while True:
    n = input("Введите натуральное число N: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

result = is_trace_of_square_of_symmetric_matrix(n)
print(f"Cимметричной матрицa? - {result}")
