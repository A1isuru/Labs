def ape(num):
    return sum(int(digit) for digit in str(num))

def brrrrr(N):
    target_sum = ape(N)
    result = []

    for i in range(1, N):
        if ape(i) == target_sum:
            result.append(i)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("нет")

while True:
    N = input("Введите a: ")
    try:
        N = int(N)

        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

brrrrr(N)