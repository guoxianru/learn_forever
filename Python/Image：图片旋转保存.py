# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    将一张图片旋转后保存
    pip install pillow
"""

from PIL import Image

# 读取图片
img = Image.open(r"test_r.jpg")
# 转化为alpha层
img_alpha = img.convert("RGBA")
# 旋转图像
rot = img_alpha.rotate(270, expand=1)
# 与旋转图像大小相同的白色区域
fff = Image.new("RGBA", rot.size, (255, 255, 255, 255))
# 使用rot作为创建一个复合图像
out = Image.composite(rot, fff, mask=rot)
# 显示图片
out.convert(img.mode).show()
# 保存图片
out.convert(img.mode).save("test_r.jpg")
