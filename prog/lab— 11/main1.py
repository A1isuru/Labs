def remove_extra_spaces(s):
    return ' '.join(s.split())


input_string = input("Введите строку с лишними пробелами: ")
print("Очищенная строка:", remove_extra_spaces(input_string))