# Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.

string = input('Введите строку >> ')
word = input('Введите искомое слово >> ')
new_word = input('Введите слово на замену >> ')

new_string = string[: string.find(word)] + new_word + string[len(string[0: string.find(word)] + word):]

print(new_string)