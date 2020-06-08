# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import traceback

import requests
from retry import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}


# 根据ip查询国家
@retry(Exception, tries=2, delay=6)
def ip_map(ip):
    url = f"http://ip-api.com/json/{ip}?fields=61439&lang=zh-CN"
    response = requests.get(url=url, headers=headers, timeout=5).json()
    print(response)


if __name__ == "__main__":
    try:
        ip_map("123.127.240.60")
    except:
        print("错误信息为:\n%s" % traceback.format_exc())
