# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image

import requests
from hashlib import md5


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode('utf8')).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


url = 'https://antirobot.tianyancha.com/captcha/verify'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': 'TYCID=1a93dff0a22111e998fbb3b981677576; undefined=1a93dff0a22111e998fbb3b981677576; ssuid=1480618176; _ga=GA1.2.903235269.1562660375; _gid=GA1.2.678477229.1562660375; RTYCID=8c47f24e88bc404ab7ab3b13ca5c2c86; CT_TYCID=5a82281d672d4165aabaad01bbe2fda0; aliyungf_tc=AQAAAKe+mUtoxwwAuuz5cvNR0ONBk/gZ; csrfToken=n8V850lntGgDlmNhGBsbXb0o; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522Quiet.G%2522%252C%2522integrity%2522%253A%252214%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjczMDQwNCwiZXhwIjoxNTk0MjY2NDA0fQ.2zBJJKHsaiKU0xzoZEVQiqGqNHA71PRJaisM13uymfI0f78HZZdQER0XuiRQLHX29z9B9sKdy6AMrExA5M2Amg%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjczMDQwNCwiZXhwIjoxNTk0MjY2NDA0fQ.2zBJJKHsaiKU0xzoZEVQiqGqNHA71PRJaisM13uymfI0f78HZZdQER0XuiRQLHX29z9B9sKdy6AMrExA5M2Amg; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562730407; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562730407',
}

# 使用copy()防止修改原代码定义dict
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
print(ele.location)
# 定位元素的长宽
print(ele.size)
# 获取左边坐标
left = ele.location['x']
# 获取上边坐标
top = ele.location['y']
# 获取右边坐标
right = ele.size['width'] + left
# 获取下边坐标
height = ele.size['height'] + top
# 定位截图位置
print("{'left': %s, 'top': %s, 'right': %s, 'height': %s}" % (left, top, right, height))
# 打开截取文件
im = Image.open(os.getcwd() + '\\' + 'fullpage.png')
# 截图指定尺寸图片
img = im.crop((left, top, right, height))
# 保存截图文件
img.save(os.getcwd() + '\\' + 'verify.png')

# 用户中心>>软件ID 生成一个替换 96001
chaojiying = Chaojiying_Client('gxr940301', 'gbt73016.', '899869')
# 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
verify_img = open('verify.png', 'rb').read()
# 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
res = chaojiying.PostPic(verify_img, 9004)
print(res)
zuobiao_list = res['pic_str'].split('|')
print(zuobiao_list)

ele = pjdr.find_element_by_xpath("//div[@class='new-box94']")
for zuobiao in zuobiao_list:
    zb = zuobiao.split(',')
    print(zb)
    ActionChains(pjdr).move_to_element_with_offset(ele, zb[0], zb[1]).click().perform()
    time.sleep(1)
pjdr.find_element_by_id('submitie').click()
time.sleep(5)
with open('zmy.html', 'w+', encoding='utf-8') as f:
    f.write(pjdr.page_source)
