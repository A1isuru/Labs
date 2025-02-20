import random

def write_numbers_to_file(filename, N):
    with open(filename, 'w') as file:
        for _ in range(N):
            number = random.uniform(-100, 100) 
            file.write(f"{number}\n")

def find_max_odd_absolute(filename):
    max_abs_value = None
    with open(filename, 'r') as file:
        for index, line in enumerate(file, start=1):
            if index % 2 != 0:  
                number = float(line.strip())
                abs_value = abs(number)
                if max_abs_value is None or abs_value > max_abs_value:
                    max_abs_value = abs_value
    return max_abs_value

filename = "numbers.txt"
N = int(input("Введите количество чисел (N): "))

write_numbers_to_file(filename, N)
print(f"{N} чисел записано в файл '{filename}'.")

max_abs_value = find_max_odd_absolute(filename)
if max_abs_value is not None:
    print(f"Наибольшее из модулей компонентов с нечетными номерами: {max_abs_value}")
else:
    print("Файл пуст или нет компонентов с нечетными номерами.")