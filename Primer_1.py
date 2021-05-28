# !/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер кортежа")
        exit(1)
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)