#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 20 11:08'
time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
print('time:', '\n', time)
print('data:', '\n', data)
ind = data.argmax(axis=0)
print('ind:', '\n', ind)
time_max = time[ind]
print('time_max:', '\n', time_max)
data_max = data[ind, np.arange(data.shape[1])]
print('dataZ_max:', '\n', data_max)
print(np.all(data_max == data.max(axis=0)))
# 使用数组索引作为目标来赋值
a = np.arange(5)
print('a:', '\n', a)
a[[1, 3, 4]] = 0
print('a:', '\n', a)
# 当一个索引列表包含重复时，赋值被多次完成，保留最后的值
a = np.arange(5)
print('a:', '\n', a)
a[[0, 0, 2]] = [1, 2, 3]
print('a:', '\n', a)
# 使用布尔数组进行索引
a = np.arange(12).reshape(3, 4)
print('a:', '\n', a)
b = a > 4
print('b:', '\n', b)
print('a[b]:', '\n', a[b])
# 与布尔索引的第二种方法更类似于整数索引;
# 对于数组的每个维度，我们给出一个选择我们想要的切片的1D布尔数组：
a = np.arange(12).reshape(3, 4)
print('a:', '\n', a)
b1 = np.array([False, True, True])
print('b1:', '\n', b1)
b2 = np.array([True, False, True, False])
print('b2:', '\n', b2)
print('a[b1,:]:', '\n', a[b1, :])
print('a[b1]:', '\n', a[b1])
print('a[:, b2]:', '\n', a[:, b2])
print('a[b1,b2]:', '\n', a[b1, b2])