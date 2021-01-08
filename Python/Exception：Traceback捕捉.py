# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    异常捕捉打印方法
"""

import traceback

try:
    print(1 + "1")
except:
    # 异常信息作为字符串打印
    print("错误信息为:\n%s" % traceback.format_exc())
    # 异常信息打印
    print("错误信息为:\n%s" % traceback.print_exc())
    # 异常信息不打印，输出到文件
    print(
        "错误信息为:\n%s"
        % traceback.print_exc(file=open("Exception.txt", "a+", encoding="utf-8"))
    )
