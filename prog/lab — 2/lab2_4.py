x = float(input("Введите x: "))
y = float(input("Введите y: "))

if (-6 <= x <= 7) and (1 <= y <= 7) and (y <= 2 * x + 13) and (y <= (-5 * x + 38) / 3):
    print("trye")
else:
    print("folse")