# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# 中文字符串转16进制
def ChineseToUnic(c):
    return c.encode("unicode_escape").decode("utf-8")


print(ChineseToUnic("浙江淘宝网络有限公司"))

# 16进制转中文字符
def UnicToChinese(u):
    return u.encode("utf-8").decode("unicode_escape")


# 备案查询网站文字编码
print(
    UnicToChinese(
        "&#x6D59;&#x6C5F;&#x6DD8;&#x5B9D;&#x7F51;&#x7EDC;&#x6709;&#x9650;&#x516C;&#x53F8;".replace(
            "&#x", r"\u"
        ).replace(
            ";", ""
        )
    )
)
