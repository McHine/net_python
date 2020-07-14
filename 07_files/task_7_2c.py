#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv
src_file = argv[1]
dst_file = argv[2]
file_write = open(dst_file, 'w') # 'config_sw1_cleared_7_2c.txt'

file_read = open(src_file, 'r')
for line in file_read:
    ignore_string = False
    for element in ignore:
        if element in line:
            ignore_string = True
    if ignore_string == False:
        file_write.write(line)
        
file_write.close()