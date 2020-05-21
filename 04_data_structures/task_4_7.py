#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
f_part, s_part, t_part = mac.split(":")

f_part = bin(int(f_part, 16))
s_part = bin(int(s_part, 16))
t_part = bin(int(t_part, 16))
print(f_part + s_part + t_part)