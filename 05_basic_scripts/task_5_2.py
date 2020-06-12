#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# get user`s nonsense
user_data = input("Введите IP-адрес: ")

ip_and_mask = user_data.split('/')

# ---------start work with ip address-----
# retrieving an IP-address
ip_addr = ip_and_mask[0]

ap_addr_list = ip_addr.split('.')
# ---------end work with ip address-----

# ---------start work with net mask-----
# retrieving a net mask
short_net_mask = ip_and_mask[1]

# computing the number of full octets of net mask
full_octets_count = int(short_net_mask) // 8

# computing the number of bits in incomplete octet
incmplt_octet_bits = int(short_net_mask) % 8

# is octet incomplete or empty, 1 == incomplete, 0 == empty
incmplt_octet_count = int(incmplt_octet_bits > 0)

bits_value = [128, 64, 32, 16, 8, 4, 2, 1]

# computing incomplete octet value
incmplt_octet_value = str(sum(bits_value[:(incmplt_octet_bits)])) + '.'
nm_full_octet = '255.'
nm_empty_octet = '0.'

# computing the number of empty octets
empty_octets_count = 4 - full_octets_count - incmplt_octet_count


net_mask = (nm_full_octet * full_octets_count + incmplt_octet_value + nm_empty_octet * empty_octets_count).strip('.')
octets_list = net_mask.split('.')[:4]
# ---------end work with net mask-----

template = f'''
Network:
{ap_addr_list[0]:<8}  {ap_addr_list[1]:<8}  {ap_addr_list[2]:<8}  {ap_addr_list[3]:<8}
{int(ap_addr_list[0]):08b}  {int(ap_addr_list[1]):08b}  {int(ap_addr_list[2]):08b}  {int(ap_addr_list[3]):08b}

Mask:
/{short_net_mask}
{octets_list[0]:<8}  {octets_list[1]:<8}  {octets_list[2]:<8}  {octets_list[3]:<8}
{int(octets_list[0]):08b}  {int(octets_list[1]):08b}  {int(octets_list[2]):08b}  {int(octets_list[3]):08b}
'''

print(template)

