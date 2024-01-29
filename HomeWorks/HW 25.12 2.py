# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

text = input('Введите текст без запятых >> ')
words = input('Введите слова через пробел >> ')

text_list = text.split()
words_list = words.split()

for i in range(len(text_list)):
    for j in range(len(words_list)):
        if text_list[i] == words_list[j]:
            text_list[i] = words_list[j].upper()

print(' '.join(text_list))
