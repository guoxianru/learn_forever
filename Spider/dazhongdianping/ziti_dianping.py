# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
import requests
from lxml import etree
from queue import Queue
from fontTools.ttLib import TTFont


class Meishi():
    def __init__(self):
        # 请求头信息
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
            'Cookie': '_lxsdk_cuid=16c23a427a5c8-05bf4eb58e8066-e343166-144000-16c23a427a5c8; _lxsdk=16c23a427a5c8-05bf4eb58e8066-e343166-144000-16c23a427a5c8; _hc.v=a2468a58-4deb-1294-f18b-c5f7dd71833e.1563966057; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cye=beijing; cityInfo=%7B%22cityId%22%3A2%2C%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22provinceId%22%3A0%2C%22parentCityId%22%3A0%2C%22cityOrderId%22%3A0%2C%22isActiveCity%22%3Afalse%2C%22cityEnName%22%3A%22beijing%22%2C%22cityPyName%22%3Anull%2C%22cityAreaCode%22%3Anull%2C%22cityAbbrCode%22%3Anull%2C%22isOverseasCity%22%3Afalse%2C%22isScenery%22%3Afalse%2C%22TuanGouFlag%22%3A0%2C%22cityLevel%22%3A0%2C%22appHotLevel%22%3A0%2C%22gLat%22%3A0%2C%22gLng%22%3A0%2C%22directURL%22%3Anull%2C%22standardEnName%22%3Anull%7D; cy=2; _lxsdk_s=16c30f89c2c-594-351-05f%7C%7C26'
        }
        # 保持会话状态
        self.session = requests.session()
        # 城市列表
        self.city_list = []
        # 请求队列
        self.request_queue = Queue()
        # 字体库解析
        self.woff_true_dict = {}

    # 获取所有城市列表
    def get_city(self):
        city_res = self.session.get(url='http://www.dianping.com/citylist', headers=self.headers)
        city_str = re.findall(r'<!--城市列表-->(.*?)<!-- 页尾 -->', city_res.text, re.S)[0]
        self.city_list = ['http:' + i + '/ch10' for i in re.findall(r'href="(.*?)"', city_str, re.S)]

    # 把城市和类型拼接成请求url，page翻页
    def get_request(self, page):
        for city in self.city_list:
            type_res = self.session.get(url=city, headers=self.headers)
            type_html = etree.HTML(type_res.text)
            type_list = ['g' + i for i in type_html.xpath('//*[@id="classfy"]/a/@data-cat-id')]
            for p in range(1, page + 1):
                for t in type_list:
                    request_url = city + '/' + t + 'p' + str(p)
                    self.request_queue.put(request_url)
        print(self.request_queue.qsize())

    # 从指定页面获取字体库文件
    def get_woff(self, url):
        # 手动复制页面缺失字体
        with open('woff.txt', 'r', encoding='utf-8') as f:
            woff_true_str = ','.join(f.readlines())
        # 把页面缺失字体构造成列表
        woff_true_list = [i for i in woff_true_str if i != '\n' and i != ',']
        # 请求指定页面，获得最新字体库文件
        res = self.session.get(url=url, headers=self.headers)
        find_svgtextcss_url = re.search(r'href="([^"]+svgtextcss[^"]+)"', res.text, re.M)
        svgtextcss_url = find_svgtextcss_url.group(1)
        svgtextcss_url = "https:" + svgtextcss_url
        response_svgtextcss = requests.get(url=svgtextcss_url, headers=self.headers)
        # 解析当前页面字体库数量，构造列表
        woff_list = [i for i in response_svgtextcss.text.split('@font-face') if i != '']
        # 把字体库名称与url映射成字典
        woff_dict = {}
        for woff in woff_list:
            font_family = re.findall(r'font-family: "PingFangSC-Regular-(.*?)"', woff, re.S)[0]
            font_src = "https:" + re.findall(r'format\("embedded-opentype"\),url\("(.*?)"\)', woff, re.S)[0]
            woff_dict.update({font_family: font_src})
        # 把字体库文件下载到本地
        for k, v in woff_dict.items():
            down = self.session.get(url=v)
            with open(k + '.woff', 'wb+') as f:
                f.write(down.content)
            # 用字体库工具包解析字体库文件
            font = TTFont(k + '.woff')
            # # 把字体库文件转换成xml，开发环境方便查看，生产环境无用
            font.saveXML(k + '.xml')
            # 提取出字体库中所有有效字符编码
            ttglyphs = font['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
            # 把页面缺失字体与对应字符编码对应，构造字典
            self.woff_true_dict[k] = dict(zip(ttglyphs, woff_true_list))

    # 解析店铺详情
    def get_detail(self):
        # # 从请求队列取出url，发起请求
        # url = self.request_queue.get()
        shop_list_res = self.session.get(url='http://www.dianping.com/beijing/ch10/g110', headers=self.headers)
        shop_list_html = etree.HTML(shop_list_res.text)
        # 获取店铺列表
        shop_list = shop_list_html.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/@href')[:1]
        if len(shop_list) != 0:
            # 进入店铺详情页
            for shop_url in shop_list:
                shop_res = self.session.get(url='http://www.dianping.com/shop/110539724', headers=self.headers)
                shop_html = etree.HTML(shop_res.text)
                # 获取店铺网址:shop_link
                shop_link = shop_res.url
                print(shop_link)
                # 获取店铺分类:shop_type
                shop_type_str = ','.join(shop_html.xpath("string(//div[@class='breadcrumb'])").split('>')[:-1])
                shop_type = shop_type_str.replace(' ', '').replace(',', '>')
                print(shop_type)
                # 获取店铺详情
                shop_detail_list = shop_html.xpath("//div[@id='basic-info']")
                for detail in shop_detail_list:
                    # 店铺名称:shop_name
                    shop_name = detail.xpath("./h1[@class='shop-name']/text()")[0].replace(' ', '')
                    print(shop_name)
                    # 评论数量:shop_comment
                    comment1 = detail.xpath(".//span[@id='reviewCount']/text()")
                    comment2_type = detail.xpath(".//span[@id='reviewCount']/d/@class")[0]
                    comment_data = self.woff_true_dict[comment2_type]
                    comment2_str = [i.encode('unicode_escape').decode().replace('\\u', 'uni') for i in
                                    detail.xpath(".//span[@id='reviewCount']/d/text()")]
                    comment2_list = []
                    for i in comment2_str:
                        if i in comment_data.keys():
                            comment2_list.append(comment_data[i])
                    if len(comment1) == 2:
                        shop_comment = (comment1[0] + ''.join(comment2_list) + comment1[1]).replace(' ', '')
                    else:
                        shop_comment = (
                                ''.join(comment2_list)[:-1] + comment1[0] + comment1[1] + ''.join(comment2_list)[
                            -1] +
                                comment1[2]).replace(' ', '')
                    print(shop_comment)
                    # 人均价格:shop_price
                    price1 = detail.xpath(".//span[@id='avgPriceTitle']/text()")
                    price2_type = detail.xpath(".//span[@id='avgPriceTitle']/d/@class")[0]
                    price_data = self.woff_true_dict[price2_type]
                    price2_str = [i.encode('unicode_escape').decode().replace('\\u', 'uni') for i in
                                  detail.xpath(".//span[@id='avgPriceTitle']/d/text()")]
                    price2_list = []
                    for i in price2_str:
                        if i in price_data.keys():
                            price2_list.append(price_data[i])
                    if len(price1) == 2:
                        shop_price = (price1[0] + ''.join(price2_list) + price1[1]).replace(' ', '')
                    else:
                        shop_price = (price1[0] + ''.join(price2_list)[:-1] + price1[1] + ''.join(price2_list)[-1] +
                                      price1[2]).replace(' ', '')
                    print(shop_price)
                    # 口味:shop_flavor
                    # 环境:shop_ambient
                    # 服务:shop_service
                    # 地址:shop_address
                    address_data = re.findall('id="address"> (.*?)<div class="addressIcon">', shop_res.text)[0]
                    address_true = [i for i in re.findall('>(.*?)<', address_data, re.S) if i != '']
                    address_str = re.findall('class="(.*?)">(.*?);', address_data, re.S)
                    address_list = []
                    for i in address_str:
                        a = list(i)
                        a[1] = a[1].replace('&#x', 'uni')
                        address_list.append(a)
                    for i in address_list:
                        address_type_data = self.woff_true_dict[i[0]]
                        if i[1] in address_type_data.keys():
                            i[0] = address_type_data[i[1]]
                    for i in range(len(address_true)):
                        for k in address_list:
                            if k[1][-4:] == address_true[i][-5:-1]:
                                address_true[i] = k[0]
                    shop_address = ''.join(address_true)
                    print(shop_address)
                    # 电话:shop_phone
        else:
            print('没有找到符合条件的商户')


if __name__ == '__main__':
    meishi = Meishi()
    # meishi.get_city()
    # meishi.get_request(10)
    meishi.get_woff('http://www.dianping.com/shop/110539724')
    meishi.get_detail()
