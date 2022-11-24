# Task 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import os

os.system('cls')

print('К какой четверти принадлежит точка (X,Y)?')

x = int(input('Введите координату X:'))

y = int(input('Введите координату Y:'))

if x == 0 or y == 0:
    print('Точка на одной из осей координат.')

elif x > 0 and y > 0:
    print('Точка в 1 квадранте.')

elif x < 0 and y > 0:
    print('Точка во 2 квадранте.')

elif x < 0 and y < 0:
    print('Точка в 3 квадранте.')

else:
    print('Точка в 4 квадранте.')