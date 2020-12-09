# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/21 4:47 下午
software: PyCharm
文件说明：
get_url_logid处理的链接 应该从html中获取，在cookie中获取带有转发的会没有
    web端
https://weibo.com/2750720500/JryA1fgL3
https://weibo.com/1749965754/JqtyhtZSH?from=page_1006061749965754_profile&wvr=6&mod=weibotime&type=comment#_rnd1603416374132
    m端
https://m.weibo.cn/status/4562781430874746?sourceType=weixin&from=10AA195010&wm=2468_1001&featurecode=newtitle
https://m.weibo.cn/status/4562770438390221
https://m.weibo.cn/status/4562770438390221?
"""
import time, datetime
import json
import re
import requests
from broker.api_conf import api
from broker.mysql_conf import mysql
from urllib.parse import unquote

USER_AGENT = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36']
COMMENTS_BASE_URL = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type={}'
BASE_URL = 'https://m.weibo.cn/status/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36'
}

conf = {
    'api': api,
    'mysql': mysql
}


def get_today_file_name(*args):
    '''
    :param args: benteng_2 , weibo
    :return: benteng_2_weibo_2020-10-22
    '''
    return str(datetime.datetime.utcnow()).split()[0] + '_' + '_'.join(args)


def write_json(json_data, json_name, file_name):
    with open('log/'+file_name + '/' + json_name + '.json', 'w+', encoding='utf-8')as f:
        f.write(json.dumps(json_data, ensure_ascii=False, indent=4))
    print(f'write {json_name}.json file success')


def compare_data(task_data, user_list, url, type, file_name):
    url_id = get_url_logid(url)
    json_name = get_today_file_name(url_id, type)
    json_data = {
        type: user_list
    }
    write_json(json_data, json_name, file_name)

    new_task_data = []
    for task in task_data:
        if task['staff_nick_name'] in user_list:
            task['result'] = {"status": True}
            new_task_data.append(task)
    return new_task_data


def get_url_logid(url):
    logid = ''
    if '://m.weibo.cn' not in url:
        try:
            if '?' not in url:
                base_id = url.split('/')[-1]
            else:
                base_id = re.findall('(.*?)\?', url.split('/')[-1])[0]
        except:
            print(f'erro message: {url}')
            return None
        response = requests.get(BASE_URL + base_id, headers=HEADERS)

        for cookie in response.cookies:
            if 'M_WEIBOCN_PARAMS' == cookie.name:
                value = unquote(cookie.value)
                print(value)
                logid = re.findall("&fid=(.*?)&", value)[0]
        if logid == '':
            try:
                logid = re.findall('"mid": "(.*?)"', response.text)[0]
            except:
                print(f"get logid error,url :{url}")

    else:
        if '?' not in url:
            logid = url.split('/')[-1]
        else:
            logid = re.findall('(.*?)\?', url.split('/')[-1])[0]

    return logid


def write_error_txt(file_name,data):
    with open('log/'+file_name + '/error_data.txt', 'a+', encoding='utf-8')as f:
        f.write(str(datetime.datetime.now()).split('.')[0] + '   ' + file_name + '   ' + json.dumps(data,
                                                                                                    ensure_ascii=False) + '\n')

if __name__ == '__main__':
    pass
    from parse import parse
    import os
    file_name = get_today_file_name('benteng', 'weibo')
    print('log/'+file_name)
    if not os.path.exists('log/'+file_name):
        print('------')
        os.mkdir(os.path.join(os.getcwd(),'log', file_name))