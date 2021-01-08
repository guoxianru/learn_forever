# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    自动提取字符串中的地区信息
    pip install cpca
    pip install folium
"""

import cpca
from cpca import drawer

# 以列表格式传入待解析地区信息
location_str = [
    "深圳市南山区蛇口燕山路12号万联大厦B座7-AB室",
    "中国上海市草包路2401号百得亭4楼",
    "中国上海市浦东新区张江高科技园区金科路2966号1栋405室，邮编201203",
]

# 分词模式，解析出的信息是DataFrame格式
df1 = cpca.transform(location_str)
print(df1)

# 全文模式，解析出的信息是DataFrame格式
df2 = cpca.transform(location_str, cut=False)
print(df2)

# 将解析出的地区信息传入函数，画出地图，以HTML格式存储浏览
drawer.draw_locations(df1, "df1.html")
