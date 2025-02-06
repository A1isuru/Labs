def gi(num):
    return sum(int(digit) for digit in str(num))

def fu(n, m):
    result = []

    for i in range(1, n+1):
        if gi(i) ** 2 == m:
            result.append(i)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("нет")

while True:
    n = input("Введите n: ")
    b = input("Введите m: ")
    try:
        n = int(n)
        b = int(b)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

fu(n, b)