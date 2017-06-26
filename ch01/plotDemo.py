#!python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'wangjj'
__mtime__ = '2017 06 24 17:26'
x = np.linspace(-5, 5, 200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y)) * 1.5
# 绘图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, yn, c='blue', marker='o')
ax.plot(x, y + 0.75, 'r')
plt.show()
# 树


