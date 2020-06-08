# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

# 实例化一个ChromeOptions对象
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 在调用浏览器驱动时传入option参数就能实现undefined
driver = webdriver.Chrome(options=options)
# 最大化窗口
driver.maximize_window()
# 打开淘宝首页
driver.get('https://www.taobao.com')
# 等待页面加载
driver.implicitly_wait(3)
# 点击登陆按钮
driver.find_element_by_link_text('亲，请登录').click()
# 随机休眠0-1秒
time.sleep(random.random())
# 点击使用密码登陆
driver.find_element_by_id('J_Quick2Static').click()
# 随机休眠0-1秒
time.sleep(random.random())
# 找到用户名输入框
user = driver.find_element_by_id('TPL_username_1')
# 随机休眠0-1秒
time.sleep(random.random())
# 清空用户名输入框
user.clear()
# 随机休眠0-1秒
time.sleep(random.random())
# 输入用户名
user.send_keys('update')
# 找到密码输入框
password = driver.find_element_by_id('TPL_password_1')
# 随机休眠0-1秒
time.sleep(random.random())
# 清空密码输入框
password.clear()
# 随机休眠0-1秒
time.sleep(random.random())
# 输入密码
password.send_keys('update')
# 如果出现滑块验证码
try:
    # 滑块验证码
    huakuai = driver.find_element_by_id('nc_1_n1z')
    action = ActionChains(driver)
    action.click_and_hold(huakuai).perform()
    for index in range(200):
        try:
            # 平行移动鼠标
            action.move_by_offset(50, 0).perform()
        except UnexpectedAlertPresentException:
            break
        action.reset_actions()
        # 随机休眠0-1秒
        time.sleep(random.random())
except:
    pass
