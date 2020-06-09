# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import os
import time
import json
import requests
import logging
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from scrapy import signals

from .settings import USER_AGENT_URL, COOKIE_URL, PROXY_URL
from .extra_tools.chaojiying import Chaojiying_Client


class TianyanchaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TianyanchaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        if response.url[:47] == 'https://antirobot.tianyancha.com/captcha/verify':
            # 验证码URL
            url = response.url
            # 请求头
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
                'Connection': 'keep-alive',
                'Cookie': '',
            }
            # 添加请求头，使用copy()防止修改原代码定义dict
            cap = DesiredCapabilities.PHANTOMJS.copy()
            for key, value in headers.items():
                cap['phantomjs.page.customHeaders.{}'.format(key)] = value
            # 调用无头浏览器
            pjdr = webdriver.PhantomJS(desired_capabilities=cap)
            # 窗口最大化
            pjdr.maximize_window()
            # 访问地址
            pjdr.get(url)
            # 定位图片位置
            ele = pjdr.find_element_by_xpath("//div[@class='new-box94']")
            # 生成保存图片路径
            picpath = os.getcwd() + '\\' + 'fullpage.png'
            # 保存当前访问页面快照
            pjdr.save_screenshot(picpath)
            # 定位选取元素坐标
            # print(ele.location)
            # 定位元素的长宽
            # print(ele.size)
            # 获取左边坐标
            left = ele.location['x']
            # 获取上边坐标
            top = ele.location['y']
            # 获取右边坐标
            right = ele.size['width'] + left
            # 获取下边坐标
            height = ele.size['height'] + top
            # 定位截图位置
            # print("{'left': %s, 'top': %s, 'right': %s, 'height': %s}" % (left, top, right, height))
            # 打开截取文件
            im = Image.open(os.getcwd() + '\\' + 'fullpage.png')
            # 截图指定尺寸图片
            img = im.crop((left, top, right, height))
            # 保存截图文件
            img.save(os.getcwd() + '\\' + 'verify.png')
            # 调用超级鹰，用户中心>>软件ID 生成一个替换 96001
            chaojiying = Chaojiying_Client('gxr940301', 'gbt73016.', '899869')
            # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
            verify_img = open('verify.png', 'rb').read()
            # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
            res = chaojiying.PostPic(verify_img, 9004)
            # 超级鹰返回信息
            # print(res)
            # 提取坐标列表
            zuobiao_list = res['pic_str'].split('|')
            # print(zuobiao_list)
            # 调用浏览器模拟点击验证码
            ele = pjdr.find_element_by_xpath("//div[@class='new-box94']")
            for zuobiao in zuobiao_list:
                zb = zuobiao.split(',')
                print(zb)
                ActionChains(pjdr).move_to_element_with_offset(ele, zb[0], zb[1]).click().perform()
                time.sleep(1)
            # 提交点击
            pjdr.find_element_by_id('submitie').click()
            # 等待页面跳转加载
            time.sleep(5)
            # 把返回的页面源码返回
            response = pjdr.page_source
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CookieMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.user_agent_url = USER_AGENT_URL
        self.cookie_url = COOKIE_URL

    def get_user_agent(self):
        try:
            response = requests.get(self.user_agent_url)
            if response.status_code == 200:
                user_agent = response.text
                return user_agent
        except requests.ConnectionError:
            return False

    def get_cookies(self):
        try:
            response = requests.get(self.cookie_url)
            if response.status_code == 200:
                cookies = json.loads(response.text)
                return cookies
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        # self.logger.debug('正在获取Cookies')
        # cookies = self.get_cookies()
        cookies = {'aliyungf_tc': 'AQAAAKe+mUtoxwwAuuz5cvNR0ONBk/gZ',
                   'csrfToken': 'n8V850lntGgDlmNhGBsbXb0o',
                   'TYCID': '1a93dff0a22111e998fbb3b981677576',
                   'undefined': '1a93dff0a22111e998fbb3b981677576',
                   'ssuid': '1480618176',
                   'bannerFlag': 'undefined',
                   'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1562730407',
                   'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1562730407',
                   'tyc-user-info': '%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522Quiet.G%2522%252C%2522integrity%2522%253A%252214%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjczMDQwNCwiZXhwIjoxNTk0MjY2NDA0fQ.2zBJJKHsaiKU0xzoZEVQiqGqNHA71PRJaisM13uymfI0f78HZZdQER0XuiRQLHX29z9B9sKdy6AMrExA5M2Amg%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D',
                   'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjczMDQwNCwiZXhwIjoxNTk0MjY2NDA0fQ.2zBJJKHsaiKU0xzoZEVQiqGqNHA71PRJaisM13uymfI0f78HZZdQER0XuiRQLHX29z9B9sKdy6AMrExA5M2Amg',
                   '_ga': 'GA1.2.903235269.1562660375',
                   '_gid': 'GA1.2.678477229.1562660375',
                   'RTYCID': '8c47f24e88bc404ab7ab3b13ca5c2c86',
                   'CT_TYCID': '5a82281d672d4165aabaad01bbe2fda0',
                   }
        if cookies:
            request.cookies = cookies
            # self.logger.debug('使用Cookies：%s' % json.dumps(cookies))

        # user_agent = self.get_user_agent()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        if user_agent:
            # self.logger.debug('使用User_Agent：%s' % user_agent)
            request.headers['User-Agent'] = user_agent


class ProxyMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = PROXY_URL

    def get_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        if request.meta.get('retry_times'):
            proxy = self.get_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理：%s' % proxy)
                request.meta['proxy'] = uri
