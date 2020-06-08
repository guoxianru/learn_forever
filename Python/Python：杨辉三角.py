# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    编写函数，接收一个整数t为参数，打印杨辉三角前t行
"""


def demo(num):
    print([1])
    print([1, 1])
    line = [1, 1]
    for i in range(2, num):
        r = []
        for j in range(0, len(line) - 1):
            r.append(line[j] + line[j + 1])
        line = [1] + r + [1]
        print(line)


demo(int(input("打印行数：")))
