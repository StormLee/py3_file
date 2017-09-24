#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 20:56
# @Author  : Aries
# @Site    : cook_book def
# @File    : 0828_1.py
# @Software: PyCharm

# * list位置参数
# ** key关键字参数
import html

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
print(avg(1,2,3,4))

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' %item for item in attrs.items()]
    print(keyvals)
    attr_str = ''.join(keyvals)
    print(attr_str)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

s = make_element('item', 'Albatross', size='large', quantity=6)
print(s)

def recv(maxsize, *, block):
    'rec'
    pass
recv(1023,block=True)

def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m
print(mininum(1,5,2,10))
print(mininum(1,-5,2,10,clip=0))
# print(help(recv))

def myfun(x,y):
    return x,y,3
a,b,c = myfun(6,2)
print(a,b,c)

_no_value = object()
def spam(a,b=_no_value):
    if b is _no_value:
        print('a')
spam(1)
spam(1,2)
spam(1,None)

add = lambda x,y : x+y
print(add(2,3))
print(add('hello','world'))

names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
key=lambda x: x.split()[-1].lower()
print(key('David Beazley'))

















