# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import json
import time
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains


# 重写联众打码的api
def catch():
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
    api_username = 'username',
    api_password = 'password'
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
    def __init__(self):
        url = 'https://passport.bilibili.com/login'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    def send(self):
        self.driver.implicitly_wait(6)
        username_input = self.driver.find_element_by_id('login-username')
        username_input.clear()
        username_input.send_keys('username')

        password_input = self.driver.find_element_by_id('login-passwd')
        password_input.clear()
        password_input.send_keys('password')

        # 需要注意的东西是有多个class_name的话，只取其中一个就可以了
        # 如此处 class="btn btn-login" 只取出 btn-login 即可
        login_button = self.driver.find_element_by_class_name('btn-login')
        login_button.click()

    def scream_catch(self):
        self.driver.get_screenshot_as_file('whole_scream.png')
        element = self.driver.find_element_by_class_name('geetest_absolute')
        # print(element.location)
        # print(element.size)

        # 因为滑块每次出现的位置都是一样的，所以定死的取出图片的位置即可
        # 用Fireworks获取图片所在的坐标(x,y)
        left = 1108
        top = 321
        right = left + 314
        bottom = top + 195

        im = Image.open('whole_scream.png')
        # 在全屏的截图中取出验证码的所在位置
        im = im.crop((left, top, right, bottom))

        # 估计是因为屏幕的原因，从全屏截取出来的验证码的尺寸是等比例放大了的
        # 但是必须用和网页中验证码的尺寸相等的图片来提交给打码平台
        # 重塑图片的尺寸大小
        im = im.resize((253, 155), Image.ANTIALIAS)
        im.save('yan_zheng_ma.png')
        # 调用打码平台的api
        json_data = catch()
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
            print(offset)
            # 经过多次调试发现，如果两个坐标的y值之差大于7就会左偏 |c - d|的偏差
            if offset >= 7:
                x_offset += offset
            print(x_offset)
            return x_offset
        else:
            # 经过多次调试发现，打码平台有时候会返回没有'|'的字符串，而此时里面的第一个数就是距离
            x_offset = string.split(',')[0]
            return int(x_offset)

    def slip_button(self):
        x = self.scream_catch()
        # 滑动的动作链
        handler = self.driver.find_element_by_class_name('geetest_slider_button')
        ActionChains(self.driver).click_and_hold(handler).perform()
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        # 此处一定要睡，如果不睡的话，可能还没拉到那个位置就直接进行下一步的动作了
        time.sleep(1.5)
        ActionChains(self.driver).click().perform()

    def run(self):
        self.send()
        # 睡一下，等验证码完全加载出来，不然可能截出来是验证码没加载好的截图
        time.sleep(2)
        self.slip_button()


if __name__ == '__main__':
    login = Login()
    login.run()
