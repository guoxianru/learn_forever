import json
import os
import re

import requests
from selenium import webdriver


def get_html():
    url = "https://car.autohome.com.cn/config/series/59.html#pvareaid=3454437"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"
    }

    with requests.get(url=url, headers=headers, timeout=3) as res:
        html = res.content.decode("utf-8")

    return html


def get_detail(html):
    config = re.search("var config = (.*?)};", html, re.S)
    # option = re.search("var option = (.*?)};", html, re.S)
    js_list = re.findall("(\(function\([a-zA-Z]{2}.*?_\).*?\(document\);)", html)

    # 处理汽车参数
    car_info = ""
    # if config and option :
    #     car_info = car_info + config.group(0) + option.group(0)
    # 只要config参数，其他的参数获取方式是一致的

    if config:
        car_info = car_info + config.group(0)
    write_html(js_list, car_info)


def write_html(js_list, car_info):
    # 运行JS的DOM -- 这部破解是最麻烦的，非常耗时间~参考了互联网上的大神代码
    DOM = (
        "var rules = '2';"
        "var document = {};"
        "function getRules(){return rules}"
        "document.createElement = function() {"
        "      return {"
        "              sheet: {"
        "                      insertRule: function(rule, i) {"
        "                              if (rules.length == 0) {"
        "                                      rules = rule;"
        "                              } else {"
        "                                      rules = rules + '#' + rule;"
        "                              }"
        "                      }"
        "              }"
        "      }"
        "};"
        "document.querySelectorAll = function() {"
        "      return {};"
        "};"
        "document.head = {};"
        "document.head.appendChild = function() {};"
        "var window = {};"
        "window.decodeURIComponent = decodeURIComponent;"
    )

    # 把JS文件写入到文件中去
    for item in js_list:
        DOM = DOM + item
    html_type = "<html><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /><head></head><body>    <script type='text/javascript'>"
    # 拼接成一个可以运行的网页
    js = html_type + DOM + " document.write(rules)</script></body></html>"
    # 再次运行的时候，请把文件删除，否则无法创建同名文件，或者自行加验证即可
    with open("./demo.html", "w", encoding="utf-8") as f:
        f.write(js)

    # 通过selenium将数据读取出来，进行替换
    driver = webdriver.PhantomJS()
    driver.get("./demo.html")
    # 读取body部分
    text = driver.find_element_by_tag_name("body").text
    # 匹配车辆参数中所有的span标签
    span_list = re.findall("<span(.*?)></span>", car_info)  # car_info 是我上面拼接的字符串

    # 按照span标签与text中的关键字进行替换
    for span in span_list:
        # 这个地方匹配的是class的名称  例如 <span class='hs_kw7_optionZl'></span> 匹配   hs_kw7_optionZl 出来
        info = re.search("'(.*?)'", span)
        if info:
            class_info = (
                str(info.group(1)) + "::before { content:(.*?)}"
            )  # 拼接为  hs_kw7_optionZl::before { content:(.*?)}
            content = re.search(class_info, text).group(1)  # 匹配文字内容，返回结果为 "实测""油耗""质保"

            car_info = car_info.replace(
                str("<span class='" + info.group(1) + "'></span>"),
                re.search('"(.*?)"', content).group(1),
            )
    print(car_info)


if __name__ == "__main__":
    html = get_html()
    get_detail(html)
