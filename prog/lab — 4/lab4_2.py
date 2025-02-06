import math
while True:
    a = input("Введите x: ")
    b = input("Введите n: ")
    try:
        a = float(a)
        b = int(b)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

num = 0
for i in range(1,b+1):
    num += math.sin(a)**i
    print(num)

print(f"сумарное число: {num}")