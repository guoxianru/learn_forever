# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    全角和半角字符互相转化
"""


def have_dbc(strs):
    """
    判断字符串是否含有全角字符
    strs：待判断字符串
    特殊情况：半角空格32，全角空格12288
    返回格式：有：True  没有：False
    """
    for str in strs:
        inside_code = ord(str)
        if inside_code == 12288:
            return True
        elif 65281 <= inside_code and inside_code <= 65374:
            return True
        else:
            continue
    return False


def have_sbc(strs):
    """
    判断字符串是否含有半角字符
    strs：待判断字符串
    特殊情况：半角空格32，全角空格12288
    返回格式：有：True  没有：False
    """
    for str in strs:
        inside_code = ord(str)
        if inside_code == 32:
            return True
        elif 33 <= inside_code and inside_code <= 126:
            return True
        else:
            continue
    return False


def dbc_to_sbc(strs):
    """
    全角字符转半角字符
    strs：待转换字符串
    特殊情况：半角空格32，全角空格12288
    返回格式：转换完毕的新字符串
    """
    restrs = ""
    for str in strs:
        inside_code = ord(str)
        if inside_code == 12288:
            inside_code = 32
        elif 65281 <= inside_code and inside_code <= 65374:
            inside_code -= 65248
        restrs += chr(inside_code)
    return restrs


def sbc_to_dbc(strs):
    """
    半角字符转全角字符
    strs：待转换字符串
    特殊情况：半角空格32，全角空格12288
    返回格式：转换完毕的新字符串
    """
    restrs = ""
    for str in strs:
        inside_code = ord(str)
        if inside_code == 32:
            inside_code = 12288
        elif 33 <= inside_code and inside_code <= 126:
            inside_code += 65248
        restrs += chr(inside_code)
    return restrs


print(have_dbc("你好ｐｙｔｈｏｎａｂｄａｌｄｕｉｚｘｃｖｂｎｍ——　——"))
print(have_sbc('你好pythonabdalduizxcvbnm—— ——。“”""'))
print(dbc_to_sbc("你好ｐｙｔｈｏｎａｂｄａｌｄｕｉｚｘｃｖｂｎｍ——　——"))
print(sbc_to_dbc('你好pythonabdalduizxcvbnm—— ——。“”""'))
