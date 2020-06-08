# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import json
import time
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains


# 重写联众打码的api
def liangzhong():
    '''
            main() 参数介绍
            api_username    （API账号）               --必须提供
            api_password    （API账号密码）           --必须提供
            file_name       （需要识别的图片路径）     --必须提供
            api_post_url    （API接口地址）           --必须提供
            yzm_min         （识别结果最小长度值）     --可空提供
            yzm_max         （识别结果最大长度值）     --可空提供
            yzm_type        （识别类型）              --可空提供
            tools_token     （工具或软件token）        --可空提供
    '''
    api_username = '',
    api_password = ''
    file_name = 'yan_zheng_ma.png'
    api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    yzm_min = ''
    yzm_max = ''
    yzm_type = '1310'
    tools_token = ''

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    print(r.text)
    return r.text


class Login(object):
    def __init__(self, username, password):
        self.url = 'https://www.tianyancha.com/login'
        self.username = username
        self.password = password
        self.brower = webdriver.Chrome()
        self.brower.maximize_window()

    def send(self):
        # 打开登录页面
        self.brower.get(self.url)
        # 等待5秒
        time.sleep(5)
        # 点击密码登录
        login_password = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]')
        login_password.click()
        # 等待5秒
        time.sleep(5)
        # 输入用户名
        username_input = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/input')
        username_input.clear()
        username_input.send_keys(self.username)
        # 等待5秒
        time.sleep(5)
        # 输入密码
        password_input = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/input')
        password_input.clear()
        password_input.send_keys(self.password)
        # 等待5秒
        time.sleep(5)
        # 点击登录按钮
        login_button = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]')
        login_button.click()
        # 等待5秒
        time.sleep(5)
        # 点击获取有缺口图片
        yzm_button = self.brower.find_element_by_xpath('/html/body/div[10]/div[2]/div[2]/div[2]/div[2]')
        yzm_button.click()
        # 等待5秒
        time.sleep(5)

    def get_yzm(self):
        # 整页截图
        self.brower.get_screenshot_as_file('whole_page.png')
        # 定位验证码图片
        element = self.brower.find_element_by_class_name('gt_box')
        # 因为滑块每次出现的位置都是一样的，所以把图片的位置定死，用PS获取图片所在的坐标(x,y)
        left = 785
        top = 371
        right = 1107
        bottom = 516
        # 在全屏的截图中取出验证码的所在位置
        im = Image.open('whole_page.png')
        im = im.crop((left, top, right, bottom))
        # 还原图片原尺寸
        im = im.resize((element.size['width'], element.size['height']), Image.ANTIALIAS)
        im.save('yan_zheng_ma.png')
        # 调用打码平台的api
        json_data = liangzhong()
        json_data = json.loads(json_data)
        string = json_data['data']['val']
        if '|' in string:
            a, b = string.split('|')
            a, c = a.split(',')
            b, d = b.split(',')
            x_offset = int(a) - int(b)
            offset = int(c) - int(d)
            # 返回值的第一个数和第三个数之差的绝对值就是要滑动的距离
            x_offset = x_offset if x_offset > 0 else -x_offset
            offset = offset if offset > 0 else -offset
            # 经过多次调试发现，如果两个坐标的y值之差大于7就会左偏 |c - d|的偏差
            if offset >= 7:
                x_offset += offset
            return x_offset
        else:
            # 经过多次调试发现，打码平台有时候会返回没有'|'的字符串，而此时里面的第一个数就是距离
            x_offset = string.split(',')[0]
            return int(x_offset)

    def slip_button(self, x):
        # 滑动的动作链
        handler = self.brower.find_element_by_xpath('/html/body/div[10]/div[2]/div[2]/div[2]/div[2]')
        ActionChains(self.brower).click_and_hold(handler).perform()
        time.sleep(1)
        ActionChains(self.brower).move_by_offset(xoffset=x, yoffset=0).perform()
        # 此处一定要睡，如果不睡的话，可能还没拉到那个位置就直接进行下一步的动作了
        time.sleep(1.5)
        ActionChains(self.brower).click().perform()

    def get_cookies(self):
        verifiy_str = '<style>@charset'

        x = self.get_yzm()
        print('第一次滑动距离：%s' % x)
        self.slip_button(x)
        # 等待5秒
        time.sleep(5)
        # 验证是否通过
        if verifiy_str in self.brower.page_source:
            return self.brower.get_cookies()

        x += 5
        print('第二次滑动距离：%s' % x)
        self.slip_button(x)
        # 等待5秒
        time.sleep(5)
        # 验证是否通过
        if verifiy_str in self.brower.page_source:
            return self.brower.get_cookies()

        x -= 10
        print('第三次滑动距离：%s' % x)
        self.slip_button(x)
        # 等待5秒
        time.sleep(5)
        # 验证是否通过
        if verifiy_str in self.brower.page_source:
            return self.brower.get_cookies()

        return None

    def run(self):
        self.send()
        print(self.get_cookies())
        self.brower.close()


if __name__ == '__main__':
    login = Login('', '')
    login.run()
