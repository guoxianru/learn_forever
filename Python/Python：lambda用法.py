# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    lambda用法
"""


# 有名函数
def fun(x, y, z):
    return x + y + z


print(fun(1, 2, 3))

# 使用匿名函数但有名字
f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

# 匿名函数
print((lambda x, y, z: x + y + z)(1, 2, 3))


# 匿名函数默认值参数
g = lambda x, y=2, z=3: x + y + z
print(g(1))


# 匿名函数关键字参数
g = lambda x, y=2, z=3: x + y + z
print(g(1, z=4, y=1))
