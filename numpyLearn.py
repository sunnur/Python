import numpy as np
pi = np.pi
"""
#print("hello world")

#建立矩阵、数组
x = np.array([1,2,3])
print(x)

#dtype 为 numpy的属性，表示数据类型
print(x.dtype)

#创建U8类型的矩阵
x = np.uint8([1,2,3])
print(x)
print(x.dtype)

#1~2，step为0.1的矩阵
print(np.arange(1, 2, 0.1))

#0~2pi，元素个数为100的矩阵
print(np.linspace(0, 2 * pi, 100))

#创建0矩阵
print(np.zeros((3,3), np.uint8))

#创建全1矩阵
print(np.ones((3,3), np.uint8))

#创建单元矩阵
print(np.eye((3), dtype = np.uint8))
print(np.identity((3), dtype = np.uint8))

#创建随机数矩阵，取值范围0~256，大小8*8，数据类型U8
print(np.random.randint(0, 256, (8, 8), np.uint8))

A = np.ones((3,3), dtype = np.uint8)
#变形
print(A.reshape(1,9))

#扁平化
print(A.flatten())
print(A.ravel())

B = np.random.randint(0,4,(3,4))
#print("B = \n",B)
#转置
print(B.T)

#横向堆叠
print(np.hstack([A,B]))
"""

A = np.ones((3,3), dtype = np.uint8)
B = np.random.randint(0,4,(3,4))
#矩阵点乘
print(A)
print(B)
C = A @ B
print(C)
C = A.dot(B)
print(C)