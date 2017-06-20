import numpy as np

a = np.arange(15).reshape(3, 5)
print(type(a))
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
# 创建数组的几种方法
# array
b = [2, 3, 4]
b = np.array(b)
print(b)
c = [(1, 2, 3), (5, 6, 7)]
print(c)
print(np.array(c))
d = [((1, 2, 3), (4, 5, 6)), ((7, 8, 9), (10, 11, 12)),
     ((13, 14, 15), (16, 17, 18))]
print(d)
nd = np.array(d)
print(nd)
print(nd.shape)
# 数组类型可以在创建时显示指定
e = np.array([[1, 2], [3, 4]], dtype=complex)
print(e)
# 使用占位符创建数组的函数
f = np.zeros((3, 4))
print(f)
g = np.ones((2, 3, 4), dtype=np.int16)
print(g)
h = np.empty((2, 3))
print(h)
# 为了创建一个数列，NumPy提供一个类似range的函数返回数组而不是列表:
i = np.arange(10, 30, 5)
print(i)
# 当 arange 使用浮点数参数时，由于有限的浮点数精度，通常无法预测获得的元素个数。
# 因此，最好使用函数 linspace 去接收我们想要的元素个数来代替用range来指定步长。
j = np.linspace(10, 30, 5)
print(j)
k = [[1, 2, 3], [4, 5, 6]]
print(type(k), '\n', np.array(k))
