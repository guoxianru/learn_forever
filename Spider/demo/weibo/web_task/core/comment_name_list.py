# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/18 2:31 下午
software: PyCharm
文件说明：被动任务，获取评论用户列表
"""
import time
import random
import json
import requests
from core.tools import USER_AGENT,COMMENTS_BASE_URL,get_url_logid



class CommentNameList(object):
    """
    CommentNameList类用于获取评论昵称
    """
    def __init__(self,url):
        """
        方法用于
        """
        self.max_id_type = 0
        self.logid = get_url_logid(url)
        self.comments_url = COMMENTS_BASE_URL.format(self.logid,self.logid,self.max_id_type)
        self.headers = {
            'x-xsrf-token': '2caf49',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': random.choice(USER_AGENT),
            'referer': 'https://m.weibo.cn/status/{}'.format(self.logid),
            'cookie': 'WEIBOCN_FROM=1110106030; loginScene=102003; SUB=_2A25yisLPDeRhGeFK41oS8SrLwj2IHXVudO6HrDV6PUJbkdAKLWfwkW1NQsJPD4NgTNhmxbPDrL9bK9-gd8TXUnMC; SUHB=0P1MHg5tbPZieU; _T_WM=94770674613; XSRF-TOKEN=e322d2; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4561669231222303%26luicode%3D20000061%26lfid%3D4561669231222303%26uicode%3D20000061%26fid%3D4561669231222303'
            # 'cookie' : 'WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25yj74XDeRhGeVK7FoQ9SrOyTmIHXVuc8JfrDV6PUJbkdANLWXxkW1NTHzFI26gb-YTHFx1czfAoyR5L1W4d4Bh; SUHB=0cSnG0AFGs7jXM; _T_WM=69823984978; XSRF-TOKEN=5765bd; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4559857535421257%26uicode%3D20000061%26fid%3D4559857535421257'
            # 'cookie': '_T_WM=17024089056; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4559857535421257%26uicode%3D20000061%26fid%3D4559857535421257; XSRF-TOKEN=709651',
        }
        self.name_list = []
        self.session = requests.session()
        self.total_number = 0


    def get_max_id_and_type(self,comment_json_data):
        if comment_json_data.get('ok') == 1:
            # print('into------')
            try:
                max_id = comment_json_data['data']['max_id']
                max_id_type = comment_json_data['data']['max_id_type']
            except Exception as e:
                print('max_id is None', e)
                print(comment_json_data)
                return False, False

            # self.total_number = comment_json_data['data']['total_number']
            datas = comment_json_data['data']['data']

            for data in datas:
                screen_name = data['user']['screen_name']
                text = data['text']
                # print(screen_name, text)
                self.name_list.append(screen_name)
            # print('*' * 100)
        else:
            max_id = 0
            max_id_type = 0

        return max_id, max_id_type

    def parse_data(self,response,comments_url):

        while True:
            comment_json_data = json.loads(response.text)

            max_id, max_id_type = self.get_max_id_and_type(comment_json_data)
            if max_id == 0:
                break

            print(f'next page id :{max_id},next max_id_type :{max_id_type},url:{comments_url}')
            response, comments_url = self.get_next_url(comments_url, max_id, max_id_type)
            # print(comment_json_data)
            time.sleep(random.randint(1, 2) + random.random())



    def get_next_url(self,url,max_id=None,max_id_type=0):

        if max_id is None:
            comments_url = url

        else:
            comments_url = COMMENTS_BASE_URL.format(self.logid, self.logid, max_id_type) + '&max_id=' + str(max_id)

        response = requests.get(comments_url,headers=self.headers)

        # max_id,max_id_type = self.parse_data(comment_json_data)

        return response,comments_url


    def run(self):

        response,comments_url = self.get_next_url(self.comments_url)
        self.parse_data(response,comments_url)

        return self.name_list


if __name__ == '__main__':
    # https://m.weibo.cn/1623340585/4559857535421257
    url = 'https://m.weibo.cn/1623340585/4559857535421257'
    # web_url = "https://weibo.com/1749965754/JpSiv57Yz?from=page_1006061749965754_profile&wvr=6&mod=weibotime&type=comment"
    web_url = 'https://m.weibo.cn/1749965754/4562138729808543'
    cnl = CommentNameList(web_url)
    print(cnl.run())

    # shijian = 'Sat Oct 17 21:16:15 +0800 2020'
    # import datetime
    # print(datetime.datetime.strftime())
    # print()


