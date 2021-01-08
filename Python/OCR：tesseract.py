# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    开源识别工具tesseract调用方法
"""


def ocr_tesserocr(img_path):
    """
    tesserocr模块调用
    依赖:需在Python环境Scripts目录下包含tesseract软件的语言包tessdata
    pip install tesserocr
    pip安装失败时可以用离线包安装
    pip install pillow
    """
    import tesserocr
    from PIL import Image

    # 打开图片
    img = Image.open(img_path)
    # 识别图片中文字,lang指定语言包识别,chi_sim为简体中文
    text = tesserocr.image_to_text(img, lang="chi_sim")
    print(text)


def ocr_pytesseract(img_path):
    """
    pytesseract模块调用
    依赖:需安装tesseract软件,添加环境变量或指定EXE路径皆可
    pip install pytesseract
    pip install pillow
    """
    import pytesseract
    from PIL import Image

    # 打开图片
    img = Image.open(img_path)
    # 指定tesseract.exe路径
    pytesseract.pytesseract.tesseract_cmd = r"D:\A下载文件\tesseract\tesseract.exe"
    # 识别图片中文字,lang指定语言包识别,chi_sim为简体中文
    text = pytesseract.image_to_string(img, lang="chi_sim")
    print(text)
