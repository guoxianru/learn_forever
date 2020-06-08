from scrapy.spiders import CrawlSpider,Request,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
import re

from demo_bloom.spiders.baseSpider import custom_base

class Gongwenku(CrawlSpider):
    name = 'gongwenk'
    start_urls = [
        # 'https://www.gongwk.com/article.jhtml'
        'https://www.gongwk.com/articles/c-22.jhtml'
    ]

    def parse(self, response):
        print('ttttttt',response.url)
        sel = Selector(response)
        num=sel.css('div#table-pagination ::attr(data-number)').extract_first()
        next_num = int(num) + 2

        if int(num):
            next_url = re.sub('(\d+)\.',str(next_num)+".",response.url)
        else:
            next_url= re.sub('.jhtml','-2.jhtml',response.url)

        #next url
        yield Request(url=next_url,priority=1,callback=self.parse)


