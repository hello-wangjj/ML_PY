#!python3
# -*- coding: utf-8 -*-
import numpy as np
__author__ = 'wangjj'
__mtime__ = '2017 06 20 22:39'
# 矩阵的行列式
A = np.mat([[1, 2, 4, 5, 7], [9, 12, 11, 8, 2],
            [6, 4, 3, 2, 1], [9, 1, 3, 4, 5], [0, 2, 3, 4, 1]])
print('det(A):', '\n', np.linalg.det(A))
# 矩阵的逆
print('inv(A):', '\n', np.linalg.inv(A))
# 矩阵的秩
print('matrix_rank(A):', '\n', np.linalg.matrix_rank(A))
print(A.ndim)
# 可逆矩阵的求解
B = [1, 0, 1, 0, 1]
print('AX=B,X=?', '\n', np.linalg.solve(A, B))
a = np.arange(9) - 4
print('norm a:', '\n', np.sqrt(sum(np.power(a, 2))))
print('norm a:', '\n', np.linalg.norm(a))
print('汉明距离')
matV = np.mat([[1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1]])
smstr = np.nonzero(matV[0] - matV[1])
print('smstr:', '\n', smstr)
print('smstr shape[0]:', '\n', (np.shape(smstr[0])))
print('相关系数计算')
x = [-2.1, -1, 4.3, 2]
y = [3, 1.1, 0.12, 3]
X = np.vstack((x, y))
mv1 = np.mean(X[0])
mv2 = np.mean(X[1])
dv1 = np.std(X[0])
dv2 = np.std(X[1])
corref = np.mean(np.multiply(X[0] - mv1, X[1] - mv2)) / (dv1 * dv2)
print(corref)
print(np.corrcoef(X))
print('协方差矩阵')
print(np.cov(X))
covinv = np.linalg.inv(np.cov(X))
A = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
evals, evecs = np.linalg.eig(A)
print('特征值：', evals)
print('特征向量：', evecs)
