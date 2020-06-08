# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import random
import asyncio
from pyppeteer import launch


# from retry import retry


async def main(user, pw, url):
    browser = await launch({
        "headless": False,
        # 重新指定临时数据路径，解决windows系统 OSError: Unable to remove Temporary User Data报错问题
        "userDataDir": r"F:\temporary",
        # 有头的不要加这句话，容易导致浏览器进程无法结束
        # "args": ['--no-sandbox'],
        # "dumpio": True 解决浏览器卡住问题
        'dumpio': True})
    """浏览器启动的时候，自动使用cookies信息或者缓存填写了账号输入框，通过系新建上下文，可以解决多个浏览器数据共享的问题，暂时没想到其他的解决方案"""
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    # page = await browser.newPage() # 启动个新的浏览器页面
    # 新定义的注入js函数每次导航或者加载新的页面时会自动执行js注入 比起page.evaluate()每打开一个页面都要单独注入一次好用
    await inject_js(page)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/72.0.3626.109 Safari/537.36')
    # goto到指定网页并且等到网络空闲为止
    await page.goto(url, {"waitUntil": 'networkidle2'})
    await page.type("#TPL_username_1", user, {"delay": input_time_random() - 50})  # 毫秒
    await page.type("#TPL_password_1", pw, {"delay": input_time_random()})
    await asyncio.sleep(random.random() + 0.5)  # 毫秒
    # 判断是否有滑块
    slider = await page.Jeval("#nocaptcha", "node => node.style")
    if slider:
        print("slider appear")
        flag, page = await mouse_slide(page=page)
        fresh = ""
        # 处理刷新重新验证的情况
        try:
            fresh = await page.Jeval(".errloading", "node => node.textContent")
        except:
            pass
        if fresh:
            # 刷新滑块验证
            await page.hover("a[href='javascript:noCaptcha.reset(1)']")
            await page.mouse.down()
            await page.mouse.up()
            await asyncio.sleep(random.uniform(1, 2))
            try:
                # page.J相当于page.querySelector()
                await page.J(".nc-lang-cnt[data-nc-lang='_startTEXT']")
                print("refresh slider success: begin verify slide again...")
                # 二次滑块验证
                flag, page = await mouse_slide(page=page)
                if flag:
                    return await click_login(page)
                else:
                    print("second verify slider faild: quit")
                    return
            except:
                print("refresh slider failed: please check your code")
                return
        if flag:
            return await click_login(page)
        else:
            print("login failed: please check out your code")
            return
    else:
        print("No slider")
        return await click_login(page)


# 点击登陆
async def click_login(page):
    """
    	1 作为一个整体，因是异步，导航等待触发，去执行点击操作，点击操作完，触发导航结束
        2 只有导航结束才能进行登陆结果判断
        3 看到其他大神写的是先按回车键，不是很明白，模拟回车键相当于登陆了，页面跳转后执行点击就会报错，所以这儿直接把回车操作干掉，有点疑惑，还希望懂的老哥指点一下
    """
    await asyncio.gather(page.waitForNavigation(), page.evaluate("document.getElementById('J_SubmitStatic').click()"))
    # 检测点击登陆后是否出现滑块验证
    try:
        slider = await page.Jeval("#nocaptcha", "node => node.style")
        if slider:
            print("after click login slider appear")
            flag, page = await mouse_slide(page)
            if flag:
                # 点击登陆出现滑块验证，密码框是被清空的，所以需要重新输入密码
                await page.type("#TPL_password_1", pwd, {"delay": input_time_random()})
                await asyncio.gather(page.waitForNavigation(),
                                     page.evaluate("document.getElementById('J_SubmitStatic').click()"))
                try:
                    await page.waitForSelector(".account-id", {"timeout": 15000})
                    print(page.url)
                    return await get_cookie(page)
                except:
                    print("timeout wait for element: .account-id")
                    return
    except:
        pass

    # 检测是否有账号密码错误
    try:
        global error
        error = await page.Jeval("#J_Message .error", "node => node.textContent")
        print("error:", error)
        print("account_info:", username)
    except Exception as e:
        error = None
    finally:
        if error:
            print("确保账号安全重新输入")
        else:
            try:
                # 等待登陆成功页面某一元素的出现
                await page.waitForSelector(".account-id", {"timeout": 10000})
                print(page.url)
                return await get_cookie(page)
            except:
                print("timeout wait for element: .account-id")


# def retry_if_result_none(result):
#   return result is None

# 这儿写重试没实际作用，如果需要的话自己加上
# @retry(retry_on_result=retry_if_result_none)
async def mouse_slide(page=None, frame=None):
    try:
        if frame:
            await frame.hover("#nc_1_n1z")
        else:
            await page.hover("#nc_1_n1z")
            await page.mouse.down()
            await page.mouse.move(2000, 0, {"delay": random.randint(1000, 2000)})
            # await page.mouse.move(2000, 0, {"steps": random.randint(50, 100)})
            await page.mouse.up()
    except Exception as e:
        print("mouse error retry... or please check your code")
        return None
    else:
        await asyncio.sleep(random.uniform(1, 2))
        # 判断是否通过
        slider_result = ""
        try:
            slider_result = await page.Jeval(".nc-lang-cnt", "node => node.textContent")
        except Exception as e:
            pass
        if slider_result != "验证通过":
            print("verify fail error info:", slider_result)
            return None, page
        else:
            print("verify pass")
            return 1, page


async def get_cookie(page):
    cookies_list = await page.cookies()
    cookies = ""
    for cookie in cookies_list:
        str_cookie = "{0}={1};"
        str_cookie = str_cookie.format(cookie["name"], cookie["value"])
        cookies += str_cookie
    return cookies


def input_time_random():
    return random.randint(100, 151)


async def inject_js(page):
    js1 = "() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }"
    js2 = "() =>{ window.navigator.chrome = { runtime: {},  }; }"
    js3 = "() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }"
    js4 = "() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }"
    await page.evaluateOnNewDocument(js1)
    await page.evaluateOnNewDocument(js2)
    await page.evaluateOnNewDocument(js3)
    await page.evaluateOnNewDocument(js4)


if __name__ == '__main__':
    username = "update"
    pwd = "update"
    url = "https://login.taobao.com/member/login.jhtml?style=mini&css_style=b2b&from=b2b&full_redirect=true&redirect_url=https://login.1688.com/member/jump.htm?target=https://login.1688.com/member/marketSigninJump.htm?Done=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&reg=%20http://member.1688.com/member/join/enterprise_join.htm?lead=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&leadUrl=http://login.1688.com/member/"
    loop = asyncio.get_event_loop()
    coroutine = main(username, pwd, url)
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)
    if task.result():
        print(task.result())
