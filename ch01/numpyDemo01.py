#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 0618 16:35'

# 打印数组
a = np.arange(6)
print(a)
b = np.arange(12).reshape(3, 4)
print(b)
# 基本运算
# 数组的算术运算是按元素的。新的数组被创建并且被结果填充。
c = np.array([20, 30, 40, 50])
d = np.arange(4)
print(c, '\n', d)
e = c - d
print(e)
print(e**2)
print(10 * np.sin(c))
print(c < 35)

# NumPy中的乘法运算符 * 指示按元素计算，
# 矩阵乘法可以使用 dot 函数或创建矩阵对象实现
f = np.array([[1, 1],
              [0, 1]])
g = np.array([[2, 0],
              [3, 4]])
print(f * g)
print(np.dot(f, g))
print(f.dot(g))
print(f * 3)
print(f + g)
f *= 3
print(f)
# 当运算的是不同类型的数组时，结果数组和更普遍和精确的已知(这种行为叫做upcast)。
h = np.ones(3, dtype=np.int32)
i = np.linspace(0, np.pi, 3)
print(h, '\n', i)
print(i.dtype.name)
j = h + i
print(j)
print(j.dtype.name)
# 许多非数组运算，如计算数组所有元素之和，被作为ndarray类的方法实现
k = np.random.random((2, 3))
print(k)
print(k.sum())
print(k.min())
print(k.max())
# 指定 axis 参数你可以吧运算应用到数组指定的轴上
l = np.arange(12).reshape(3, 4)
print(l)
print(l.sum(axis=0))
print(l.min(axis=0))
print(l.cumsum(axis=1))
# 通用函数(Universal Functions)
j = np.arange(3)
print(j)
print(np.exp(j))
print(np.sqrt(j))


