"""
    读取Excel转换为字典
    把字典添加进列表，写入Excel(表头不定，选取最长表头)
    pip install pandas
"""

import pandas as pd

# 读取Excel
df = pd.read_excel(r"test.xlsx")
# 空白用""填充
df.fillna("", inplace=True)
# 把数据转化为字典格式
res = df.to_dict(orient="records")
# 把字典写入列表中
item_list = []
for item in res:
    item_list.append(item)
# 把列表转化为DataFrame格式
pf = pd.DataFrame(item_list)
# 空白用""填充
pf.fillna("", inplace=True)
# 把数据写入Excel
pf.to_excel(r"test1.xlsx", encoding="utf-8", index=False)
