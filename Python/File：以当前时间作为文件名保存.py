# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    以当前时间作为文件名保存
"""

from datetime import datetime

# 当前时间对象
today = datetime.now()
file = "已查询结果_{}{}{}_{}{}{}.xlsx".format(
    today.year, today.month, today.day, today.hour, today.minute, today.second
)
print(file)
