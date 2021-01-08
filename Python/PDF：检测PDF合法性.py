# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    检测PDF文件是否有效，参数为pdf文件全路径名
"""


def test_pdf(pathfile):
    from PyPDF2 import PdfFileReader

    flag = True
    try:
        # 利用PyPDF2的PdfFileReader模块打开pdf文件，如果不抛异常，就认为此pdf文件有效
        reader = PdfFileReader(pathfile)
        # 进一步通过页数判断
        if reader.getNumPages() < 1:
            # PDF文件页数小于1说明文件无效
            flag = False
    except:
        flag = False
    return flag
