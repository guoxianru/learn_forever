# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    Python调用poppler方法
"""


def pdf_to_xml(exe_path, input_file, output_file):
    """
    os模块调用cmd运行转化命令
    依赖:需已下载Windows版poppler软件
    pip install tesserocr
    """
    import os

    os.system("%s -c -hidden -xml %s %s" % (exe_path, input_file, output_file))


pdf_to_xml(
    r"D:\PycharmProject\pdftotab\poppler-0.68.0\bin\pdftohtml.exe",
    r"D:\PycharmProject\pdftotab\data\test.pdf",
    r"D:\PycharmProject\pdftotab\data\text.xml",
)
