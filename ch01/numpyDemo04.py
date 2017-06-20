#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 19 21:53'
a = np.floor(10 * np.random.random((2, 12)))
print(a)
print(np.hsplit(a, 3))
# 在第三和第四列之后拆分
print(np.hsplit(a, (3, 5)))
print('--------------')
# 复制和视图
# Copies and Views
# No Copy at All
b = np.arange(12)
print(b.shape)
c = b
print(b is c)
c.shape = (3, 4)
print(b.shape)
print(id(b), '\n', id(c))
# View or Shallow Copy
print('View or Shallow Copy')
d = b.view()
print(d is b)
print(d.base is b)
print(d.flags.owndata)
d.shape = (2, 6)
print(b.shape)
print(d.shape)
print(b, '\n', d)
d[0, 4] = 1000
print(b)
# 切片数组返回它的一个视图
s = b[:, 1:3]
s[:] = 10
print(b)
print(d)
# Deep Copy
e = b.copy()
print(e is b)
print(e.base is b)
e[0, 0] = 999
print('b', b)
print('e', e)
