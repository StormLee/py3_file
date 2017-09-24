#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 23:10
# @Author  : Aries
# @Site    : 
# @File    : 01_0831_1.py
# @Software: PyCharm
from collections import ChainMap
a = {'x': 1,'z': 3}
b = {'y': 2, 'z':4}
c = ChainMap(b,a)
print(c['x'])
print(c['y'])
print(c['z'])
del c['z']
print(b)
print(c['z'])
print(list(c.keys()))
print(list(c.values()))
