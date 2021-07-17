"""
Задание №1:
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""

raw_number = input("Введите трёхзначное число: ")
raw_list = list(raw_number)
num1, num2, num3 = list(map(int, raw_list))

total_sum = num1 + num2 + num3
total_mult = num1 * num2 * num3

print(f'Введённое число: {raw_number}, сумма: {total_sum}, произведение: {total_mult}')