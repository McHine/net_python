#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.replace('O', 'OSPF')
ospf_route = ospf_route.replace(',','')
ospf_route = ospf_route.split()
ospf_route[2] = ospf_route[2].strip('[]')

ospf_headers = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

print("{:<23}{:<23}".format(ospf_headers[0], ospf_route[0]))
print("{:<23}{:<23}".format(ospf_headers[1], ospf_route[1]))
print("{:<23}{:<23}".format(ospf_headers[2], ospf_route[2]))
print("{:<23}{:<23}".format(ospf_headers[3], ospf_route[3]))
print("{:<23}{:<23}".format(ospf_headers[4], ospf_route[4]))
print("{:<23}{:<23}".format(ospf_headers[5], ospf_route[5]))
