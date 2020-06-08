# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    爬虫代理获取
"""


def wuyou_proxies():
    """
    无忧代理Https代理
    order：无忧代理IP提取码
    apiUrl：无忧代理获取IP的API接口
    """
    import requests

    order = "c714e62db21d6bfb4867ae6598ff35bb"
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
    res = requests.get(apiUrl).content.decode()
    ips = res.split("\n")
    for ip in ips:
        proxyMeta = "http://" + ip
        proxies = {"http": proxyMeta, "https": proxyMeta}

        return proxies


def aby_proxies():
    """
    阿布云HTTP隧道代理
    proxyHost：代理服务器Host
    proxyPort：代理服务器Port
    proxyUser：阿布云隧道通行证书
    proxyPass：阿布云隧道通行密钥
    返回格式：proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    """
    try:
        proxyHost = "http-pro.abuyun.com"
        proxyPort = "9010"
        proxyUser = "HPXQBMBS9H3C775P"
        proxyPass = "9A16756F6F4372DF"
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        proxies = {"http": proxyMeta, "https": proxyMeta}
    except:
        proxies = {}

    return proxies


def own_proxies():
    """
    免费代理池
    proxy_pool_url：免费代理池地址
    返回格式：proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    """
    import requests

    proxy_pool_url = "http://47.94.245.242:5010/get/"
    try:
        res = requests.get(url=proxy_pool_url).text
        proxyMeta = "http://" + res
        proxies = {"http": proxyMeta, "https": proxyMeta}
    except:
        proxies = {}

    return proxies
