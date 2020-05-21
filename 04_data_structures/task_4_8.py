#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.1'
ip_a = ip.split('.')

ip_a[0] = int(ip_a[0])
ip_a[1] = int(ip_a[1])
ip_a[2] = int(ip_a[2])
ip_a[3] = int(ip_a[3])

print("{:<10}{:<10}{:<10}{:<10}".format(ip_a[0],ip_a[1],ip_a[2],ip_a[3]))
print("{:<10b}{:<10b}{:<10b}{:<10b}".format(ip_a[0],ip_a[1],ip_a[2],ip_a[3]))
