#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
    Скрипт не должен выводить команды, в которых содержатся слова,
    которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

# from sys import argv
# filename = argv[1]


outf = open('07_files/config_sw1.txt', 'r')
for line in outf:
    if line.startswith("!"):
        continue
    elif 
            
                
