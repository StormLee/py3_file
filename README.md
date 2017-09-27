# py3_file
py code test
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 10:26
# @Author  : Aries
# @Site    : 
# @File    : 0927_1.py
# @Software: PyCharm
import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #用于
        with open('D:\\py3_file\\\pypc\\yb21.txt','wt') as f:
            f.write(r.text)
        return r.text
    except:
        return "异常"

yb21 = 'http://www.yb21.cn/'
if __name__ == '__main__':
    getHTMLText(yb21)
