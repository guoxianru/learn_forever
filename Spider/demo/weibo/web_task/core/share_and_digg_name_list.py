# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/16 3:19 下午
software: PyCharm
文件说明：被动任务：获得转发，点赞用户列表
"""
import time
import random
import json
import requests
from core.tools import USER_AGENT
from auth.weibo_cookie_seleium import weibo_login
from urllib.parse import unquote
from core.tools import get_url_logid

class PassivityTask(object):
    """
    PassivityTask类用于:微博被动任务
    """
    def __init__(self,url,key):
        """
        方法用于
        """
        logid = get_url_logid(url)
        self.share_url_part = 'https://m.weibo.cn/api/statuses/repostTimeline?id={}&page='.format(logid)
        self.digg_url_part = 'https://m.weibo.cn/api/attitudes/show?id={}&page='.format(logid)
        self.key = key

        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'SUB=_2A25ynJlXDeRhGeVK7FoQ9SrOyTmIHXVuficfrDV6PUJbkdAKLWXekW1NTHzFIy1iO6tG_mymL_UPTbXUsuX517SX; SUHB=0IIVjtkmAl35Vd; WEIBOCN_FROM=1110006030; _T_WM=14070277130',
        }
        self.name_list = []
        self.total_number = 0



    def update_cookie(self,cookie_list):
        """
        方法用于
        """
        # [{'domain': '.weibo.cn', 'expiry': 1603338103, 'httpOnly': False, 'name': 'MLOGIN', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.weibo.cn', 'httpOnly': True, 'name': 'WEIBOCN_FROM', 'path': '/', 'secure': False, 'value': '1110006030'}, {'domain': '.weibo.cn', 'expiry': 1604198503, 'httpOnly': False, 'name': '_T_WM', 'path': '/', 'secure': False, 'value': '15139775928'}]
        cookie_d = {}
        cookie_str = ''
        cookie_l = []
        for item in cookie_list:
            cookie_d[item['name']] = item['value']

            str = item['name']+'='+  unquote(item['value'])+'; '
            cookie_str += str
            cookie_l.append(item['name']+'='+  unquote(item['value']))
        cookie_s = '; '.join(cookie_l)
        return cookie_d,cookie_s


    def get_name_list(self,json_data,page_num):
        """
        方法用于
        """
        if json_data['ok'] == 1 and json_data['msg'] == '数据获取成功':
            if page_num == 1:
                self.total_number = json_data['data']['total_number']

            if json_data['data']['data'] == None:
                print(f"no data:{json_data}")
                return False

            for nick_name in json_data['data']['data']:
                self.name_list.append(nick_name['user']['screen_name'])

            return True
        else:
            print(json_data['msg'])
            return False


    def run(self):
        """
        方法用于
        """
        page_num = 1
        url_part = ''
        if self.key == 'digg':
            url_part = self.digg_url_part
        elif self.key == 'share':
            url_part = self.share_url_part

        while True:
            url_all = url_part + str(page_num)
            print(url_all)
            try:
                response = requests.get(url_all,headers=self.headers)
                # print(response.text)
            except Exception as e:
                self.headers['cookie'] = self.update_cookie()
                response = requests.get(url_all,self.headers)
            if '<!doctype html>' in response.text:
                print(url_all)
                print(response.url)

                cookie_list = weibo_login(response.url,self.headers['cookie'])
                cook,cookie_s = self.update_cookie(cookie_list)
                # print(cook)
                del self.headers['cookie']
                response = requests.get(url_all,self.headers,cookies=cook)

                self.headers['cookie'] = cookie_s

            json_data = json.loads(response.text)

            if not self.get_name_list(json_data,page_num):
                print('over')
                break
            page_num += 1
            time.sleep(random.randint(1, 2) + random.random())

        print(f"total_number:{self.total_number},name_list_number:{len(self.name_list)}")
        return self.name_list


if __name__ == '__main__':
    # url = 'https://m.weibo.cn/1749965754/4542194428682823'
    # url = 'https://m.weibo.cn/1623340585/4559857535421257'
    # url = 'https://m.weibo.cn/1749965754/4562138729808543'
    url = 'https://m.weibo.cn/1749965754/4568559026700774'
    key = 'digg'
    # key = 'share'
    ptask = PassivityTask(url,key)
    print(ptask.run())





