"""
Задание №4.
Написать программу, которая генерирует в указанных пользователем границах:

    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся
эти символы. Программа должна вывести на экран любой символ алфавита от
'a' до 'f' включительно.

"""

# Случайное целое число:
import random as rnd
raw_numbers = input('Введите через пробел два целых числа: ')
floor_int = int(raw_numbers.split()[0])
ceil_int = int(raw_numbers.split()[1])
if ceil_int < floor_int:
    step = -1
else:
    step = 1 # этот блок можно было не прописывать, т.к. шаг в 1 - по умолчанию
random_int = rnd.randint(floor_int, ceil_int, step)
print(f'Случайное целое число: {random_int}')
del raw_numbers, floor_int, ceil_int, step, random_int

# Случайное вещественное:
raw_numbers = input('Введите через пробел два вещественных числа, отделив точкой дробную часть от целой: ')
flt_floor = float(raw_numbers.split()[0])
flt_ceil = float(raw_numbers.split()[1])
seed = rnd.random()
flt_random = seed * flt_ceil + flt_floor
print(f'Случайное вещественное число: {flt_random}')
del raw_numbers, flt_floor, flt_ceil, seed, flt_random

# Случайный символ:
char_range = input('Введите через пробел диапазон символов для выдачи случайного: ')
char_floor = ord(char_range.split()[0].lower())
char_ceil = ord(char_range.split()[1].lower())
random_char = chr(rnd.randint(char_floor, char_ceil))
print(f'Случайный символ: {random_char}')
del char_range, char_floor, char_ceil, random_char

