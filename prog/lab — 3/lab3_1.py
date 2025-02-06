import math

x = float(input("Введите число x: "))

values = []

if x > 0:
    values.append(('ln(x)', math.log(x)))
else:
    print("не определен")

values.append(('sin(x)', math.sin(x)))
values.append(('cos(x)', math.cos(x)))


if values:
    sorted_values = sorted(values, key=lambda item: item[1])
    print("Значения в порядке возрастания:")
    for name, value in sorted_values:
        print(f"{name} = {value}")
else:
    print("Нет значений для вывода.")
