#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 20 0:04'
a = np.arange(12)**2
print(a)
i = np.array([1, 1, 3, 8, 5])
print(i)
print(a[i])
j = np.array([[3, 4], [9, 7]])
print('j:', j)
print('a[j]:', a[j])
palette = np.array([[0, 0, 0],                # black
                    [255, 0, 0],              # red
                    [0, 255, 0],              # green
                    [0, 0, 255],              # blue
                    [255, 255, 255]])       # white
image = np.array([[0, 1, 2, 0],           # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print('palette[image]:', palette[image])
# 我们还可以为多个维度提供索引。 每个维度的索引数组必须具有相同的形状。
b = np.arange(12).reshape(3, 4)
print('b:', b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
i = np.array([[0, 1],                        # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],                        # indices for the second dim
              [3, 3]])
print('i:', i)
print('j:', j)
print('[i,j]:', [i, j])
print('b[i,j]:', b[i, j])
print('b[i,2]:', b[i, 2])
print('b[:,j]:', b[:, j], (b[:, j]).shape)
l = [i, j]
print('b[l]:', b[l])
s = np.array([i, j])
print('s:', s)
print('tuple(s):', tuple(s))
print('b[s]:', b[tuple(s)])
