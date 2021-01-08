# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    打开一个工作簿，复制工作簿，修改新的工作簿部分内容，其余不变，写入新Excel文件
    pip install xlrd
    pip install xlutils
"""

import xlrd
from xlutils.copy import copy

# 打开工作簿
book1 = xlrd.open_workbook(r"test.xls")
# 打开工作表
sheet1 = book1.sheet_by_name("Sheet1")
# 拷贝一份原来的excel
book2 = copy(book1)
# 打开新的工作表
sheet2 = book2.get_sheet("Sheet1")
# 原表的总行数
num_rows = sheet1.nrows
# 原表的总列数
num_cols = sheet1.ncols
# 循坏修改单元格内容
for row in range(num_rows):
    for col in range(num_cols):
        # 获取单元格
        value = sheet1.cell_value(row, col)
        # 写入单元格
        sheet2.write(row, col, "")
# 保存工作簿
book2.save(r"test1.xls")
