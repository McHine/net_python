#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

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

# computing network address from IP-address
ip_addr_bin = "{:08b}{:08b}{:08b}{:08b}".format(int(ap_addr_list[0]),int(ap_addr_list[1]),int(ap_addr_list[2]),int(ap_addr_list[3]))
net_mask_length = '0' * int(short_net_mask)
network_ip_addr = ip_addr_bin[:len(net_mask_length)] + '0' * (32 - len(net_mask_length))

# network address in list; values of list element must be an integer
network_addr_list = [int(network_ip_addr[:8], 2), int(network_ip_addr[8:16], 2), int(network_ip_addr[16:24], 2), int(network_ip_addr[24:], 2)]

# done with computing network address from IP-address


template = f'''
Network:
{network_addr_list[0]:<8}  {network_addr_list[1]:<8}  {network_addr_list[2]:<8}  {network_addr_list[3]:<8}
{network_addr_list[0]:08b}  {network_addr_list[1]:08b}  {network_addr_list[2]:08b}  {network_addr_list[3]:08b}

Mask:
/{short_net_mask}
{octets_list[0]:<8}  {octets_list[1]:<8}  {octets_list[2]:<8}  {octets_list[3]:<8}
{int(octets_list[0]):08b}  {int(octets_list[1]):08b}  {int(octets_list[2]):08b}  {int(octets_list[3]):08b}
'''

print(template)
