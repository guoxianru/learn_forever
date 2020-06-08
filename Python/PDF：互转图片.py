# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    PDF文件与图片相互转化:把PDF每一页内容转化为一张图片,把几张图片合并为一个PDF文件
"""


def pdftoimg():
    """
        使用第三方库PyMuPDF
        pip install PyMuPDF
    """
    import fitz
    import glob

    # 匹配文件,返回PDF文件
    pdffile = glob.glob(r"test.pdf")[0]
    # 打开PDF文件
    doc = fitz.open(pdffile)
    # 开始页码
    strat = 0
    # 结束页码,doc.pageCount为PDF总页码
    totaling = doc.pageCount
    # 循坏转化
    for pg in range(strat, totaling):
        # 获取PDF文件单页内容
        page = doc[pg]
        # 缩放系数,此处若是不做设置，默认图片大小为：792X612, dpi=96
        rotate = int(0)
        zoom = int(100)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 保存图片
        pm.writePNG("test_%s.pdf.png" % str(pg + 1))


def imgtopdf():
    """
        使用第三方库PyMuPDF
        pip install PyMuPDF
    """
    import glob
    import fitz
    import os

    # 打开新文件
    doc = fitz.open()
    # 读取文件夹下所有图片，确保按文件名排序
    for img in sorted(glob.glob("imgs/*")):
        # 打开图片
        imgdoc = fitz.open(img)
        # 使用图片创建单页的PDF
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        # 将当前页插入文档
        doc.insertPDF(imgpdf)
    # 如果同名PDF已存在则删除
    if os.path.exists("test.pdf"):
        os.remove("test.pdf")
    # 保存pdf文件
    doc.save("test.pdf")
    # 最终关闭文档
    doc.close()


def pdfcutimg():
    """
        使用第三方库pdf2image
        依赖poppler软件，需加入环境变量
        pip install pdf2image
    """
    from pdf2image import convert_from_path

    convert_from_path(
        # PDF文件路径
        "old_file_path",
        # 图片输出路径
        output_folder="new_file_path",
        # 图片输出名称
        output_file="new_file_name",
        # 指定软件EXE路径
        poppler_path="poppler_path",
        # 转化图片格式
        fmt=".png",
    )
