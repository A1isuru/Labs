def conv(n):
    if n < 0:
        return "Ошибка: введите натуральное число (n >= 0)"
    hex_value = hex(n)[2:]  
    return hex_value

while True:
    n = input("Введите a: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

a = conv(n)
if isinstance(a, str) and "Ошибка" in a:
    print(a)
else:
    print(f"Шестнадцатеричное представление числа {n} равно: {a}")
