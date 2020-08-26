# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    中文和数值互相转化
"""

import binascii

a = "中文"
print(a)
# 中文转为bytes
b = bytes(a, encoding="utf-8")
print(b)
# bytes转为16进制
c = int(binascii.hexlify(b), 16)
print(c)
