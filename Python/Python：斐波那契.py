# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    斐波那契数字
    输入要求的是第n个数字
    正确输出第n个数
"""


def fun(n):
    if n < 0:
        print("输入有误！")
    elif n == 1 or n == 2:
        return 1
    else:
        return fun(n - 1) + fun(n - 2)


n = int(input("please input a number:"))
for i in range(1, n + 1):
    print(fun(i))
