# Task 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
import math

os.system('cls')

print('Найдем расстояние между точками на плоскости.')

a = input('Введите координату точки А в формате X пробел Y: ').split()

b = input('Введите координату точки B в формате X пробел Y: ').split()

dist = math.sqrt((int(b[0]) - int(a[0]))**2 + (int(b[1]) - int(a[1]))**2)

print(f'Расстояние между точками А и В равно: {dist}.')