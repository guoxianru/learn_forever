# -*- coding: utf-8 -*-
import re
import scrapy


class MeishiSpider(scrapy.Spider):
    name = 'meishi'
    # allowed_domains = ['xxx']
    start_urls = ['http://www.dianping.com/']

    def parse(self, response):
        city_list_url = 'http:' + response.xpath('//*[@id="logo-input"]/div/div[1]/a/@href')[0].extract()
        yield scrapy.Request(url=city_list_url, callback=self.parse_city_list)

    def parse_city_list(self, response):
        list_str = re.findall(r'<!--城市列表-->(.*?)<!-- 页尾 -->', response.text, re.S)[0]
        url_list = ['http:' + i + '/ch10' for i in re.findall(r'href="(.*?)"', list_str, re.S)]
        print(url_list)
