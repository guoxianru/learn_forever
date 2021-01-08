# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    运行SQL语句从数据库读取数据写入Excel
    pip install pandas
    pip install pymysql
"""

import pandas as pd
import pymysql

# 连接数据库
conn = pymysql.Connect(
    host="127.0.0.1", port=3306, user="root", passwd="1111", db="cisscool"
)
# 通过SQL语句获取数据
df = pd.read_sql("SELECT * FROM ciss_components", con=conn)
# 把数据写入Excel
writer = "test.xlsx"
df.to_excel(writer, encoding="utf-8", index=False)
