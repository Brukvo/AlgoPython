"""
Задание №8.
Определить, является ли год, который ввел пользователем, високосным или невисокосным.

"""
year = int(input('Введите год: '))
if year % 4 != 0:
    print(f'{year} год - НЕ високосный.')
else:
    print(f'{year} год - високосный.')