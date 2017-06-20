#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 19 20:30'
# 索引，切片和迭代
# 一维 数组可以被索引、切片和迭代，就像 列表 和其它Python序列。
a = np.arange(10)**3
print(a)
print(a[0], a[2])
print(a[2:5])
print(a[:7:2])
a[:7:2] = -27
print(a)
print(a[::-1])
for i in a:
    print(i**(1 / 3))


def f(x, y):
    print(x, '\n', y)
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(b, '\n', b.dtype.name)
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3, :])
# 当少于轴数的索引被提供时，确失的索引被认为是整个切片：
# the last row. Equivalent to b[-1,:]
print(b[-1])
c = np.array([
    [[0, 1, 2], [10, 11, 12]],
    [[100, 101, 102], [110, 111, 112]]
])
print('------------------')
print(c)
print(c.shape)
print(c[1, ...])
print(c[1, :, :])
print(c[..., 2])
print(c[:, :, 2])
print(c[:, 1, :])
print('------------------')
# 迭代 多维数组是就第一个轴而言的
for row in c:
    print(row)
# 如果一个人想对每个数组中元素进行运算，我们可以使用flat属性，该属性是数组元素的一个迭代器
for element in c.flat:
    print(element)
