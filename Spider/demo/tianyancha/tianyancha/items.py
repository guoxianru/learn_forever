# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaItem(scrapy.Item):
    # 企业ID
    uuid = scrapy.Field()
    # 企业名称
    name = scrapy.Field()
    # 天眼查链接
    href = scrapy.Field()
    # 联系方式
    lxfs = scrapy.Field()
    # 工商信息
    gsxx = scrapy.Field()
    # 主要人员
    zyry = scrapy.Field()
    # 股东信息
    gdxx = scrapy.Field()
    # 对外投资
    dwtz = scrapy.Field()
