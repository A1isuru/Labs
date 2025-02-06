while True:
    a = input("Введите сумму стипендии A (в рублях): ")
    b = input("Введите начальные расходы B (в рублях): ")
    try:
        a = float(a)
        b = float(b)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное число.")

r = 0.03 
n = 10    
total_expenses = 0

for i in range(n):
    monthly_expenses = b * (1 + r) ** i
    total_expenses += monthly_expenses

total_scholarship = a * n
amount_needed = total_expenses - total_scholarship

if amount_needed > 0:
    print(f"Сумма, которую следует попросить у родителей: {amount_needed:.2f} рублей.")
else:
    print("Стипендии достаточно для покрытия расходов.")
