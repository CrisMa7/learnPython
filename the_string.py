#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 求增长的百分比
s1 = 72
s2 = 85
r = (s1-s2)/72*100
print('%.1f%%'%r)
#中文编码
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
