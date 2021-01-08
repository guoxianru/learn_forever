# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    阶乘的实现方法
"""

# 原始一个函数实现
def fun(n):
    mul = 1
    for i in range(1, n + 1):
        mul *= i
    return mul


# 使用递归方法实现
def func(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * func(n - 1)


print(fun(5))
print(func(5))
