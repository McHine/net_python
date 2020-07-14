#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv
filename = argv[1]
file_for_write = open('config_sw1_cleared.txt', 'w')

outf = open(filename, 'r')
for line in outf:
    ignore_string = False
    for element in ignore:
        if element in line:
            ignore_string = True
    if ignore_string == False:
        file_for_write.write(line)
        
file_for_write.close()
