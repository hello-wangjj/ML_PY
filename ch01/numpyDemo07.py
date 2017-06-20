#!python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'wangjj'
__mtime__ = '2017 06 20 14:18'
# 线性代数
# 简单阵列操作
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print('a:', '\n', a)
print('a.transpose:', '\n', a.transpose())
print(a.T)
print('np.linalg.inv(a)', '\n', np.linalg.inv(a))
u = np.eye(2)
print('u:', '\n', u)
j = np.array([[0.0, -1.0], [1.0, 0.0]])
print('j:', '\n', j)
# 内积：np.dot(a,b) 就可以来计算a，b的内积
print(np.dot(a, j))
print(' np.trace(u)', '\n', np.trace(u))
y = np.array([[5.], [7.]])
# solve用于解线性方程组AX==B。
print('y:', '\n', y)
print('np.linalg.solve(a, y):', '\n', np.linalg.solve(a, y))
# eig 求解特征值 特征向量
print('np.linalg.eig(j)', '\n', np.linalg.eig(j))
print('np.linalg.eig(u)', '\n', np.linalg.eig(u))
# 技巧和技巧
# “Automatic” Reshaping
print('技巧和技巧')
a = np.arange(30)
a.shape = 2, -1, 3
print(a.shape)
# Histograms
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# 建立方差为0.5 ^ 2，平均值为2的10000个正态偏差向量
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1)
plt.show()
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, density=1)  # NumPy version (no plot)
print(bins)
print(.5 * (bins[1:] + bins[:-1]))
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()
