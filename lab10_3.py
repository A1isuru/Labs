import random

def generate_table(n, m):
    table = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]
    return table

def find_longest_sequence_row(table):
    max_length = 0
    max_row_index = -1

    for row_index, row in enumerate(table):
        current_length = 1
        max_current_length = 1

        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                current_length += 1
            else:
                current_length = 1

            max_current_length = max(max_current_length, current_length)

        if max_current_length > max_length:
            max_length = max_current_length
            max_row_index = row_index

    return max_row_index

def print_table(table):
    for row in table:
        print(row)


while True:
    n = input("Введите натуральное число N: ")
    m = input("Введите натуральное число M: ")
    try:
        n = int(n)
        m = int(m)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

table = generate_table(n, m)
print_table(table)

longest_sequence_row = find_longest_sequence_row(table)
print(f"Номер строки с самой длинной последовательностью одинаковых элементов: {longest_sequence_row}")
