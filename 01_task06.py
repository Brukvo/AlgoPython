"""
Задание №6.
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

"""
first_letter = ord('a')
letter_num = int(input('Введите номер буквы латинского алфавита: '))
letter_pos = first_letter + letter_num - 1
letter = chr(letter_pos)
print(f'На позиции {letter_num} стоит символ {letter}.')
