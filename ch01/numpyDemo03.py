#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 19 21:19'
# 形状操作
# 更改数组的形状
a = np.floor(np.random.random((3, 4)) * 10)
print(a)
# flatten the array
print(a.ravel())
b = a.reshape(6, 2)
print(b)
c = a.T
print(c)
a.resize((6, 2))
print(a)
# 组合(stack)不同的数组
d = np.floor(np.random.random((2, 2)) * 10)
e = np.floor(np.random.random((2, 2)) * 10)
print('----------------')
print(d, '\n', e)
print(np.vstack((d, e)))
print(np.row_stack((d, e)))
print(np.hstack((d, e)))
print(np.column_stack((d, e)))
f = np.array([4., 2.])
g = np.array([3., 8.])
print('---------------')
print(f[:, np.newaxis])
# 当使用数组作为参数时，r_和c_在其默认行为中类似于vstack和hstack，但允许使用可选参数来指定要连接的轴号。
print(np.r_[1: 4, 1, 2])
