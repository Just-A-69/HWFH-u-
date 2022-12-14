# ДЗ на четверг:
# Простейший калькулятор с введением двух чисел типа float.
# Ввод с клавиатуры: операция +-/* (при желании ^√!), два числа
# Каждая операция является функцией
# Обработать деление на ноль
# В качестве завершения программы использовать операцию 0
# Название ДЗ: Ivanov_12.py

# Вариант номер раз
# while True:
#     action = input('Введите операцию: ')
#     if action == '0':
#         break
#     num_1 = float(input('Введите первое число: '))
#     num_2 = float(input('Введите второе число: '))
#     def prod(a, b): return a * b
#     def division(a, b): return a / b
#     def subtraction(a, b): return a - b
#     def total(a, b): return a + b
#     if action == '+':
#         print(total(num_1, num_2))
#     elif action == '-':
#         print(subtraction(num_1, num_2))
#     elif action == '*':
#         print(prod(num_1, num_2))
#     elif action == '/':
#         try:
#             print(division(num_1, num_2))
#         except ZeroDivisionError:
#             print('На ноль делить нельзя')
#
# Вариант номер два
# def prod(a, b): return a * b
# def division(a, b): return a / b
# def subtraction(a, b): return a - b
# def total(a, b): return a + b
# def power(a, b): return a**b  # степень числа
# def sqrt(a): return a ** 0.5  # √ числа
# def fac(a):  # факториал числа
#     f = 1
#     for a in range(2, a + 1):
#         f *= a
#     return f
#
#
# while True:
#     action = input('Введите операцию: ')
#     if action == '0':
#         break
#     num_1 = float(input('Введите первое число: '))
#     if action == '!':
#         if int(num_1) >= 0:
#             print(fac(int(num_1)))
#             continue
#     elif action == '^':
#         print(sqrt(num_1))
#         continue
#     num_2 = float(input('Введите второе число: '))
#     if action == '+':
#         print(total(num_1, num_2))
#     elif action == '-':
#         print(subtraction(num_1, num_2))
#     elif action == '*':
#         print(prod(num_1, num_2))
#     elif action == '/':
#         try:
#             print(division(num_1, num_2))
#         except ZeroDivisionError:
#             print('На ноль делить нельзя')
#     elif action == '**':
#         print(power(num_1, num_2))
