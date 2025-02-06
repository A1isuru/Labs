import math
while True:
    a = input("Введите a: ")
    b = input("Введите b: ")
    h = input("Введите h: ")
    try:
        a = float(a)
        b = int(b)
        h = int(h)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

print(f"| {'x':<10} | {'f(x)':<20}|")
print("-" * 30)

x = a
while x <= b:
    f_x = 2 * math.tan(x / 2) + 1
    print(f"| {x:<10} | {f_x:<20.5f}|")
    x += h