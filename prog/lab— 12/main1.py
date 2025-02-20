def get_initial_letters(text):
    words = text.split()
    initial_letters = set(word[0].lower() for word in words if word)
    return initial_letters

input_text = input("Введите текст: ")

initials = get_initial_letters(input_text)

print("Буквы, с которых начинаются слова в тексте:", initials)