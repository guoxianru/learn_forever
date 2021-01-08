# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    把一个非2的偶数，拆分成两个素数的和，要求如果不是偶数输出“不是偶数”，如果是偶数，则打印所有的可能结果
"""
from math import sqrt

num = int(input("输入一个大于2偶数:"))


def shu(n):
    flag = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


if num % 2 == 0:
    if num > 2:
        for a in range(3, num // 2 + 1):
            if shu(a) and shu(num - a):
                print(a, num - a)
    else:
        print("输入范围有误！")
else:
    print("不是偶数！")
