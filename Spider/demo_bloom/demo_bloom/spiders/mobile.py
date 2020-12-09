# -*- coding: utf-8 -*-
import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
