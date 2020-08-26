# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    记录函数运行时间
"""

import time


def func_time(func):
    def inner(*args, **kw):
        # 开始时间
        start_time = time.time()
        func(*args, **kw)
        # 结束时间
        end_time = time.time()
        print("函数运行时间为：", end_time - start_time, "s")

    return inner
