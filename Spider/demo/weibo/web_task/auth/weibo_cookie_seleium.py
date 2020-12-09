from selenium import webdriver
import time, requests, json

from requests.utils import cookiejar_from_dict, dict_from_cookiejar
import os, platform


def weibo_login(url, old_cookies):
    cookies_old = {}
    cookies_list = old_cookies.split(";")
    for cookie_str in cookies_list:
        k, v = cookie_str.split("=")
        cookies_old[k] = v
    try:
        sys_name = platform.system()
        executable_path = None
        for web_path in os.listdir():
            if web_path.find("chromedriver") != -1:
                if sys_name == "Darwin":
                    executable_path = "./{}".format(web_path)
                else:
                    executable_path = web_path
                break

        if not executable_path:
            web = None
            print("请把webdriver名字给为chromedriver")
            return [cookies_old]
        web = webdriver.Chrome(executable_path=executable_path)
        web.get(url)
        # time.sleep(2)
        web.delete_all_cookies()
        # time.sleep(3)

        for cookie in cookies_old.items():
            k, v = cookie
            # cookie = {'domain': '.weibo.cn',  'name': k, 'path': '/', 'secure': False, 'value': v}
            cookie = {
                "domain": ".weibo.cn",
                "expiry": int(time.time()),
                "httpOnly": True,
                "name": k.strip(),
                "path": "/",
                "secure": False,
                "value": v.strip(),
            }
            web.add_cookie(cookie)
        web.get(url)
        while 1:
            go_next = input("确认验证是否已经完成页面已刷新完成?(yes/no)")
            if go_next == "yes":
                break
            elif go_next == "no":
                continue
            else:
                break
            time.sleep(1)
        return web.get_cookies()
    except:
        return [cookies_old]
    finally:
        if web:
            web.quit()


if __name__ == "__main__":

    # print(os.listdir())
    # print(platform.system())
    cookies_test = [
        {
            "domain": ".weibo.cn",
            "expiry": 1603246675,
            "httpOnly": True,
            "name": "M_WEIBOCN_PARAMS",
            "path": "/",
            "secure": False,
            "value": "uicode%3D20000061%26fid%3D4559857535421257%26oid%3D4559857535421257",
        },
        {
            "domain": ".m.weibo.cn",
            "expiry": 1603247275,
            "httpOnly": False,
            "name": "XSRF-TOKEN",
            "path": "/",
            "secure": False,
            "value": "078553",
        },
        {
            "domain": ".weibo.cn",
            "expiry": 1634782075,
            "httpOnly": False,
            "name": "SUHB",
            "path": "/",
            "secure": True,
            "value": "0D-1hlM7qGK8Nm",
        },
        {
            "domain": ".weibo.cn",
            "expiry": 1604110075,
            "httpOnly": False,
            "name": "_T_WM",
            "path": "/",
            "secure": False,
            "value": "35674500912",
        },
        {
            "domain": ".weibo.cn",
            "expiry": 1634782075,
            "httpOnly": True,
            "name": "SUB",
            "path": "/",
            "sameSite": "None",
            "secure": True,
            "value": "_2A25yi-erDeRhGeNK4lIY-CfLzzSIHXVud4njrDV6PUJbkdAKLVHykW1NSSvy5TzwfjlI-lI8cov4QysEJt7mpKiy",
        },
        {
            "domain": ".weibo.cn",
            "expiry": 1603249675,
            "httpOnly": False,
            "name": "MLOGIN",
            "path": "/",
            "secure": False,
            "value": "1",
        },
        {
            "domain": ".weibo.cn",
            "expiry": 1603246359,
            "httpOnly": True,
            "name": "loginScene",
            "path": "/",
            "secure": False,
            "value": "102003",
        },
        {
            "domain": ".weibo.cn",
            "httpOnly": True,
            "name": "WEIBOCN_FROM",
            "path": "/",
            "secure": False,
            "value": "1110006030",
        },
    ]

    request_cookies = {}
    for cookie in cookies_test:
        request_cookies[cookie["name"]] = cookie["value"]

    print(request_cookies)

    url = "https://m.weibo.cn/login?backURL=https%3A%2F%2Fm.weibo.cn%2Fstatus%2F4559857535421257"
    re_cookies = {
        "_T_WM": "17024089056",
        "WEIBOCN_FROM": "1110006030",
        "MLOGIN": "0",
        "M_WEIBOCN_PARAMS": "oid%3D4559857535421257%26luicode%3D20000061%26lfid%3D4559857535421257%26uicode%3D20000061%26fid%3D4559857535421257",
        "XSRF-TOKEN": "709651",
    }
    url = "https://m.weibo.cn/status/4559857535421257"
    # url = 'https://m.weibo.cn/api/attitudes/show?id=4559857535421257&page=11&x-xsrf-token=2caf49&x-requested-with=XMLHttpRequest&user-agent=Mozilla/5.0+(X11;+Linux+x86_64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/34.0.1847.137+Safari/4E423F&referer=https://m.weibo.cn/status/4559857535421257&cookie=SUHB=0D-1hlM7qGK8Nm;+_T_WM=35674500912;+MLOGIN=1;+XSRF-TOKEN=6ed05b'
    # print(weibo_login(url,cookies_test))
    # headers = {
    #     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    #     'Referer': 'https://m.weibo.cn/status/4559857535421257'
    # }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "MWeibo-Pwa": "1",
        "Referer": "https://m.weibo.cn/status/4559857535421257",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "0d50",
    }
    "https://m.weibo.cn/status/4559857535421257"
    test_url = "https://m.weibo.cn/comments/hotflow?id=4559857535421257&mid=4559857535421257&max_id=138846927100901&max_id_type=0"
    # resp = requests.get(test_url,cookies=request_cookies,verify=False,headers=headers)
    # print(resp.json())
    localtime = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(int(1603349789000 / 1000))
    )
    print(localtime)
