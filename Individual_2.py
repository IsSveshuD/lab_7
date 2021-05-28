#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#2. В списке, состоящем из вещественных элементов, вычислить:
#1) сумму положительных элементов списка;
#2) произведение элементов списка, расположенных между максимальным по модулю и
# минимальным по модулю элементами.
#Упорядочить элементы списка по убыванию.
import sys

if __name__ == '__main__':
# Ввести список одной строкой.

    A = tuple(map(float, input("Введите список: ").split()))
    if not A:
          print("Заданный список пуст", file=sys.stderr)
          exit(1)

    s = sum([a for a in A if a > 0 ])
    print(s)

    a_min = a_max = A[0]
    i_min = i_max = 0
    for i, item in enumerate(A):
         it = abs(item)
         if it < a_min:
             i_min, a_min = i, it
         if it >= a_max:
             i_max, a_max = i, it

    if i_min > i_max:
         i_min, i_max = i_max, i_min

    count = 1
    for ite in A[i_min+1:i_max]:
        count *= ite
        print('Произведениие элементов между максимальным по модулю и минимальным по модулю элементами: ',count)

    g = sorted(A, reverse=True)
    print(f'Элементы списка по убыванию: {g}')