#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")

    for i, c in enumerate(s):
        if i % 2 == 0 and s[i] != " ":
            s = s.replace(s[i], "ы", 1)
    print(s)
