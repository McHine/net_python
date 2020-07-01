#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")

ip_in_octets = ip_address.split('.')

octets = []

for octet in ip_in_octets:
    octets.append(int(octet))


if octets[0] > 0 and octets[0] <= 223:
    print('unicast')
elif octets[0] > 223 and octets[0] <= 239:
    print('multicast')
elif ip_address == '255.255.255.255':
    print('local broadcast')
elif ip_address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')