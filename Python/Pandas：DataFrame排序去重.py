# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    获取已有工作表的颜色
    pip install pandas
    pip install pymysql
"""

import pymysql
import pandas as pd

# 连接数据库
mydb = pymysql.connect(
    host="127.0.0.1", user="root", passwd="1111", db="cisscool", charset="utf8"
)
# 获取游标
cur = mydb.cursor()
# 通过SQL语句读取数据
df = pd.read_sql("SELECT * FROM ciss_param_values", con=mydb)
# 根据两个字段排序
df = df.sort_values(by=["component_id", "power"])
# 一份将数据转为字典
res_1 = df.to_dict()
# 根据两个字段判重,重复返回True
df_dupl = df.duplicated(["component_id", "power"])
# 第二份转为字典
res_2 = df_dupl.to_dict()
for k, v in res_2.items():
    # 结果为Ttue是重复的
    if v is True:
        # 获取主键值
        pid = res_1["id"][k]
        # 根据主键值删除重复记录
        sql = "DELETE FROM ciss_param_values WHERE id=%s" % pid
        cur.execute(sql)
# 关闭游标
cur.close()
# 关闭数据库连接
mydb.close()
