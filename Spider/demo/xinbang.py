import random

import requests


def get_md5(string):
    import hashlib

    m = hashlib.md5()
    b = string.encode(encoding="utf-8")
    m.update(b)
    return m.hexdigest()


def get_random():
    string = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    result = random.sample(string, 9)
    return "".join(result)


def get_login(account, password, nonce, xyz):
    session = requests.Session()
    get_login = "https://www.newrank.cn/user/login"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    session.get(get_login, headers=headers)
    post_login = "https://www.newrank.cn/nr/user/login/loginByAccount"
    params = {
        "account": account,
        "password": password,
        "state": "1",
        "nonce": nonce,
        "xyz": xyz,
    }
    response = requests.post(post_login, data=params)
    print(response.text)


if __name__ == "__main__":
    account = "17621766071"
    pwd = "admin123456"
    password = get_md5(get_md5(pwd) + "daddy")
    nonce = get_random()
    xyz_string = (
        "//nr/user/login/loginByAccount?"
        "AppKey=joker&account={}&password={}&state=1&nonce={}".format(
            account, password, nonce
        )
    )
    xyz = get_md5(xyz_string)
    get_login(account, password, nonce, xyz)
