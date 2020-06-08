# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    调用翻译接口方法
"""


def baidutrans(q):
    """
    百度翻译开放平台API
    q：传入待翻译内容
    appid：百度翻译开放平台APP ID
    secretKey：百度翻译开放平台密钥
    api：百度翻译开放平台接口
    fromLang：原文语种
    toLang：译文语种
    返回格式：已翻译内容(字符串)
    """
    import json
    import random
    import urllib
    import hashlib
    import http.client

    appid = ""
    secretKey = ""
    httpClient = None
    api = "/api/trans/vip/translate"
    fromLang = "en"
    toLang = "zh"
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = (
        api
        + "?appid="
        + appid
        + "&q="
        + urllib.parse.quote(q)
        + "&from="
        + fromLang
        + "&to="
        + toLang
        + "&salt="
        + str(salt)
        + "&sign="
        + sign
    )
    try:
        httpClient = http.client.HTTPConnection("api.fanyi.baidu.com")
        httpClient.request("GET", myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        res = result.get("trans_result", "")[0].get("dst", "")
    except:
        res = ""
    finally:
        if httpClient:
            httpClient.close()

    return res


def aliyuntrans(q):
    """
    阿里云翻译开放平台API
    q：传入待翻译内容
    AccessKey ID：阿里云账号的AccessKey ID
    Access Key Secret：阿里云账号Access Key Secret
    返回格式：已翻译内容(字符串)
    """
    import json
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkalimt.request.v20181012 import TranslateGeneralRequest

    try:
        # 创建AcsClient实例
        client = AcsClient(
            # 阿里云账号的AccessKey ID
            "",
            # 阿里云账号Access Key Secret
            "",
            # 地域ID
            "cn-hangzhou",
        )
        # 创建request，并设置参数
        request = TranslateGeneralRequest.TranslateGeneralRequest()
        request.set_SourceLanguage("en")
        request.set_SourceText(q)
        request.set_FormatType("text")
        request.set_TargetLanguage("zh")
        request.set_method("POST")
        # 发起API请求并显示返回值
        response = client.do_action_with_exception(request)
        string = response.decode("utf-8")
        res = json.loads(string)["Data"]["Translated"]
    except:
        res = ""

    return res


def googletrans(q):
    """
    Google翻译开放平台API
    q：传入待翻译内容
    api：Google翻译开放平台接口
    返回格式：已翻译内容(字符串)
    """
    import requests

    try:
        api = (
            "http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q="
            + str(q)
        )
        response = requests.get(url=api)
        res = response.json()[0][0][0]
    except:
        res = ""

    return res
