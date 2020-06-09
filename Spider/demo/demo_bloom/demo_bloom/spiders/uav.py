from scrapy.spiders import CrawlSpider,Request,Rule
from scrapy.linkextractors import LinkExtractor
from demo_bloom.items import DemoBloomItem

from demo_bloom.spiders.baseSpider import custom_base

class Uav(CrawlSpider):
    name = 'uav'
    start_urls =[
        'https://www.81uav.cn/uav-news/'
    ]
    rules = (
        Rule(LinkExtractor(allow=r'https://www.81uav.cn/uav-news/index-htm-page-[0-6].html'),follow=True,process_request='change_request'),
        Rule(LinkExtractor(allow=r'https://www.81uav.cn/uav-news/\d{6}/\d+/\d+.html'),follow=False,callback='parse_item')
    )
    custom_settings = {
        "SCHEDULER_DUPEFILTER_KEY":'uav_key'
    }
    def change_request(self,request):
        # request
        request.priority=1
        return request


    def parse_item(self, response):
        print('ttttt',response.url)
        print(response.css('h1::text'))



        pass
