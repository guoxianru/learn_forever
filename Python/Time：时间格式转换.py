# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    时间格式转换
"""

import time

date = "2019-01-02 22:31"
print(date)
date_obj = time.strptime(date, "%Y-%m-%d %H:%M")
print(date_obj)
date_str = time.strftime("%Y{}%m{}%d{}%H{}%M{}", date_obj).format(
    "年", "月", "日", "时", "分"
)
print(date_str)

time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(type(time_str), time_str)
