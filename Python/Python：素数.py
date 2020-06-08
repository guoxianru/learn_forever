# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    判断是否是素数
    param n: 要判断的偶数
    return flag: 是则返回True 否则返回False
"""


def isPrime(n):
    flag = True
    if n == 1:
        flag = False
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


alist = [1, 23, 4, 5, 6, 7, 8, 9]

print(list(filter(isPrime, alist)))
