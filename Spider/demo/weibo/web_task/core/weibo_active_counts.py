# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/17 3:30 下午
software: PyCharm
文件说明：主动任务，获得点赞数，评论数，转发数
json数据借口
https://m.weibo.cn/statuses/extend?id=4559857535421257

    ---------------10月26日更新-----------------
    https://m.weibo.cn/status/4562770438390221?
    如果评论点赞转发都为0的话，会没有json获取的借口
    需要从html中获取

    "reposts_count": 1818,      share
    "comments_count": 2736,     comment
    "attitudes_count": 118975,  digg
"""
import random
import json
import re
import requests
import time
from core.tools import USER_AGENT, get_url_logid


class AtiveTask(object):
    """
    InitiativeTask类用于:微博主动任务
    """

    def __init__(self, url):
        """
        方法用于
        """
        logid = get_url_logid(url)
        self.url = 'https://m.weibo.cn/status/{}'.format(logid)
        # self.url = base_url.format(logid)
        self.extend_url = 'https://m.weibo.cn/statuses/extend'
        self.params = (
            ('id', logid),
        )

        self.headers = {
            'user-agent': random.choice(USER_AGENT),
            'referer': 'https://m.weibo.cn/status/{}?'.format(logid),
            'cookie': 'SUB=_2A25ynJlXDeRhGeVK7FoQ9SrOyTmIHXVuficfrDV6PUJbkdAKLWXekW1NTHzFIy1iO6tG_mymL_UPTbXUsuX517SX; SUHB=0IIVjtkmAl35Vd; _T_WM=18351249165; MLOGIN=1; WEIBOCN_FROM=1110006030; XSRF-TOKEN=c80023; M_WEIBOCN_PARAMS=oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4563840677187728%26uicode%3D20000061%26fid%3D4559857535421257'
            # 'cookie': 'WEIBOCN_FROM=1110106030; SUB=_2A25ykeybDeRhGeVK7FoQ9SrOyTmIHXVuffTTrDV6PUJbkdAKLVTdkW1NTHzFIw5ZjHdhTILREE4DIfq1wg4k0jer; SUHB=0C1CH6XtQm3i9M; _T_WM=42106474954; MLOGIN=1; XSRF-TOKEN=2bc131; M_WEIBOCN_PARAMS=oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4559857535421257%26uicode%3D20000061%26fid%3D4559857535421257',
            # 'cookie': '_T_WM=17024089056; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4559857535421257%26uicode%3D20000061%26fid%3D4559857535421257; XSRF-TOKEN=709651',
        }

    def update_cookie(self):
        """
        方法用于
        """
        cookie = input('需要更新cookie')
        return cookie

    def extend_run(self):
        """
        方法用于
        """
        try:
            response = requests.get(self.extend_url, headers=self.headers, params=self.params)
            print(response.request.url)

        except Exception as e:
            self.headers['cookie'] = self.update_cookie()
            response = requests.get(self.extend_url, headers=self.headers, params=self.params)
        if '微博不存在或暂无查看权限' in response.text:
            return None
        try:
            json_data = json.loads(response.text)
        except:
            print(self.extend_url, self.params)
        print('原创任务-------------', json_data)
        if json_data['ok'] == 1 and json_data['data']['ok'] == 1:
            # well_done = True
            time.sleep(random.randint(1, 2) + random.random())
            return {
                "result": {
                    "status": True,
                    "count": [{
                        "digg_count": json_data['data'].get('attitudes_count'),  # 点赞
                        "comment_count": json_data['data'].get('comments_count'),  # 评论
                        "share_count": json_data['data'].get('reposts_count')  # 转发
                            }]
                        }
                    }
        else:
            print('No data!')
            return None

    def run(self):

        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 404:
            print(response.request.url,'IP被禁，睡眠十分钟…………')
            time.sleep(600 + random.randint(1,10))
            response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            if '微博-出错了' in response.text :
                print(f'error message: 微博-出错了,url:{self.url}')
                # https://m.weibo.cn/3763879510/4563956314933499
                return None
            try:
                time.sleep(random.randint(1, 4) + random.random())

                return {
                    "result": {
                        "status": True,
                        "count": [{
                            "digg_count": re.findall('"attitudes_count": (\d+),', response.text)[0],  # 点赞
                            "comment_count": re.findall('"comments_count": (\d+),', response.text)[0],  # 评论
                            "share_count": re.findall('"reposts_count": (\d+),', response.text)[0]  # 转发
                        }]
                    }
                }

            except Exception as e:
                print(self.url, e)
                with open('error.html', 'w+', encoding='utf-8')as f:
                    f.write(response.text)
                return self.extend_run()

        else:
            return None


if __name__ == '__main__':
    # https://m.weibo.cn/1623340585/4559857535421257
    # url = 'https://m.weibo.cn/1623340585/4559857535421257'
    # https://m.weibo.cn/statuses/extend?id=4559857535421257
    # url = 'https://m.weibo.cn/status/4563597886489909'
    url = 'https://m.weibo.cn/status/4563840677187728?'
    itask = AtiveTask(url)
    print(itask.extend_run())

