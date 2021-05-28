#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.
import sys

if __name__ == '__main__':
# Ввести список одной строкой.
    a = tuple(map(int, input().split()))
    n = 9
# Если список пуст, завершить программу.
    if len(a) != 10:
        print("Неверный размер текста", file= sys.stderr)
        exit(1)
    n = min(a for i, a in enumerate(a))
    n = a.index(n)
    if n == 9:
        print(a)
    else:
        A = a[0:n] + (a[9],) + a[n+1:9] + (a[n],)
        print(A)

