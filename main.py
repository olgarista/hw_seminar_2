# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите число: ')

def sum_digits(n):
    return sum(map(int, n.replace('.', '').replace('-', '')))
print(f'Сумма цифр равна {sum_digits(n)}')

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
res = 1

for i in range(1, n + 1):
    res *= i
    print(res)

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Введите число: '))
lst = []
for i in range(1, n + 1):
    lst.append(random.randint(-n, n))
print(lst)

f = open('file.txt')
ind1 = int(f.read(1))
ind2 = int(f.read(2))
f.close()
print(f'Indexes from file.txt: {ind1}, {ind2}')
mult = lst[ind1] * lst[ind2]
print(mult)