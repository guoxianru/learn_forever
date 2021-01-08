# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    识别PDF文件的文本信息
"""

def pdf_to_text(exe_path, input_file, output_file):
    """
    os模块调用cmd运行转化命令
    依赖:需已下载Windows版poppler软件
    """
    import os

    os.system("%s %s %s" % (exe_path, input_file, output_file))
    return output_file


print(
    pdf_to_text(
        r"D:\poppler-0.68.0\bin\pdftotext.exe",
        r"D:\FMGKGB361802_1.pdf",
        r"D:\FMGKGB361802_1.txt",
    )
)


def pdf_text(input_file):
    """
        pdfplumber模块解析PDF文本
        pip install pdfplumber
        """
    import pdfplumber

    with pdfplumber.open(input_file) as pdf:
        content = ""
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            page_content = "\n".join(page.extract_text().split("\n")[:-1])
            content = content + page_content
        return content


print(pdf_text(r"D:\FMGKGB361802_1.pdf"))
