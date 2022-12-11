# Д/З 3 Pyhton

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# def sum(list):
#     sum = 0
#     for i in range (1, len(list), 2):
#         sum += list[i]
#     return sum
# list = [2, 3, 5, 9, 3]
# result = sum(list)
# print(list)
# print(f'cумма элементов списка, стоящих на нечётной идексах = {result}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# n = int(input('Введите размер списка '))
# list = []
# list2 = []
# for i in range(n):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and n > len(list)/2:
#         n = n - 1
#         a = list[i] * list[n]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def minmax (list):
#     max_min = [ ]
#     for i in range(len(list)):
#         if list[i] % 1 != 0:
#             max_min.append(list[i] %1 )
#     return max(max_min) - min(max_min)
# list = [1.10, 1.20, 3.10, 5, 10.01]
# print(list)
# result = minmax(list)
# print(f'Разница между max и min значением дробной части элементов = {result:.2f}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите десятичное число: '))
# k = ' '
# while n > 0:
#     k = str(n % 2) + k
#     n = n // 2
# print(k)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# k = int(input('Введите число k: '))
# negofibon = [1, -1]
# fibon = [1, 1]
# for i in range(2, k):
#     list = fibon[i - 1]+fibon[i - 2]
#     fibon.append(list)
#     list2 = negofibon[i - 2] - negofibon[i -1 ]
#     negofibon.append(list2)
# negofibon.reverse()
# fibon.insert(0, 0)
# print(f' Для k = {k} => {negofibon + fibon}')
