# -*- coding: utf-8 -*-
# -*- author: GXR -*-

#  pip install cchardet
import requests
import cchardet

url = "http://zgdysj.com/html/news/20190222/30452.shtml"

html = requests.get(url)
result = cchardet.detect(html.content)

html.encoding = result["encoding"]
print(html.text)
print(html.encoding)
print(result)
