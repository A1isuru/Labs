while True:
    a = input("Введите натуральное число N: ")
    try:
        a = int(a)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

def generate_primes(a):
    g=[]
    for i in range(1,a):
        g.append(i)
    return g
a = int(input("Введите натуральное число N: "))
primes = generate_primes(a)
print(f"Простые числа не больше {a}: {primes}")
