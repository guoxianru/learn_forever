# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    selenium+pyautogui实现网页右键另存为下载文件。
    pip install pyautogui
"""

import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains

# 生产浏览器对象
browser = webdriver.Chrome()
time.sleep(1)
# 请求目标网页
browser.get("https://www.baidu.com/")
time.sleep(1)
# 定位待处理元素
button = browser.find_element_by_id("su")
time.sleep(1)
# 右键点击已定位元素
ActionChains(browser).context_click(button).click().perform()
time.sleep(1)
# 利用pyautogui.typewrite方法输入键盘按键，根据菜单进行上下移动，enter输入确定
pyautogui.typewrite(["down", "down", "down", "enter"])
time.sleep(1)
# 弹出下载框，输入确定
pyautogui.typewrite(["enter"])
time.sleep(1)
# 关闭浏览器
browser.close()
