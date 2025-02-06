import math

x = float(input("Введите значение x: "))

if 0 <= x <= 1:
    F = math.pow(x, 2) - x
elif x > 1 or x < 0:
    F = math.pow(x, 2) - math.sin(math.pi * math.pow(x, 2))


print("F(x) =", F)