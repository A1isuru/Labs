def find_longest_a_sequence(s):
    max_count = 0
    current_count = 0
    for char in s:
        if char == 'а': 
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count


input_string = input("Введите строку: ")
print("Длина самой длинной последовательности 'а':", find_longest_a_sequence(input_string))