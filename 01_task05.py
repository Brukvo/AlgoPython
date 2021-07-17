"""
Задание №5.

Пользователь вводит две буквы. Определить, на каких местах алфавита
они стоят и сколько между ними находится букв.

"""
first_letter = ord('a')
letters = input('Введите через пробел две буквы латинского алфавита: ')
floor_l = ord(letters.split()[0].lower())
ceil_l = ord(letters.split()[1].lower())

floor_l_place = floor_l - first_letter + 1
ceil_l_place = ceil_l - first_letter + 1

print(f'Первый символ стоит на {floor_l_place} месте.')
print(f'Второй символ стоит на {ceil_l_place} месте.')
print(f'Расстояние между символами: {abs(ceil_l - floor_l)} симв.')
