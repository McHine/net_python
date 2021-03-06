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
# https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D0%BA%D0%B0_%D0%BF%D0%BE%D0%B4%D1%81%D0%B5%D1%82%D0%B8#%D0%9C%D0%B0%D1%81%D0%BA%D0%B8_%D0%BF%D1%80%D0%B8_%D0%B1%D0%B5%D1%81%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BC%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_(CIDR)
# retrieving a net mask
short_net_mask = ip_and_mask[1]
net_masks = {'0':'0.0.0.0','1':'128.0.0.0', '2':'192.0.0.0','3':'224.0.0.0', '4':'240.0.0.0', '5':'248.0.0.0', '6':'252.0.0.0','7':'254.0.0.0','8':'255.0.0.0','9':'255.128.0.0','10': '255.192.0.0','11':'255.224.0.0','12':'255.240.0.0','13':'255.248.0.0','14':'255.252.0.0', '15':'255.254.0.0','16':'255.255.0.0','17':'255.255.128.0','18':'255.255.192.0','19':'255.255.224.0','20':'255.255.240.0','21':'255.255.248.0','22':'255.255.252.0','23':'255.255.254.0','24':'255.255.255.0','25':'255.255.255.128','26':'255.255.255.192','27':'255.255.255.224','28':'255.255.255.240','29':'255.255.255.248','30':'255.255.255.252','31':'255.255.255.254','32':'255.255.255.255'}

mask_octet_0 = net_masks[short_net_mask].split('.')[0]
mask_octet_1 = net_masks[short_net_mask].split('.')[1]
mask_octet_2 = net_masks[short_net_mask].split('.')[2]
mask_octet_3 = net_masks[short_net_mask].split('.')[3]


# ---------end work with net mask-----

template = f'''
Network:
{ap_addr_list[0]:<8}  {ap_addr_list[1]:<8}  {ap_addr_list[2]:<8}  {ap_addr_list[3]:<8}
{int(ap_addr_list[0]):08b}  {int(ap_addr_list[1]):08b}  {int(ap_addr_list[2]):08b}  {int(ap_addr_list[3]):08b}

Mask:
/{short_net_mask}
{mask_octet_0:<8}  {mask_octet_1:<8}  {mask_octet_2:<8}  {mask_octet_3:<8}
{int(mask_octet_0):<08b}  {int(mask_octet_1):<08b}  {int(mask_octet_2):<08b}  {int(mask_octet_3):<08b}
'''

print(template)

