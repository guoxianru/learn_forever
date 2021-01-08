# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    打开一张图片,转成base64编码,把图片的base64编码进行解码,存成图片,格式要一致
"""

import base64

# 把图片用base64.b64encode编码,并转为ASCII编码
ico_base64_data = base64.b64encode(open("img_path", "rb").read()).decode("ascii")

# 把图片base64格式数据用base64.b64decode解码
img_data = base64.b64decode(ico_base64_data)
# 用解码后的数据写成一张图片,格式要一致
with open(r"xxx.ico", "wb") as f:
    f.write(img_data)
