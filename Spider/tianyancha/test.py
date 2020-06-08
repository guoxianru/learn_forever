# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import re


def add_cookie(cookie):
    cookie_str = re.search(r"([^']+=[^']+)", cookie, re.M)
    cookie_list = cookie_str.group(1).split('; ')
    cookie_dict = {}
    for c in cookie_list:
        cookie_dict.update({c.split('=')[0]: c.split('=')[1]})
    return cookie_dict


c = 'TYCID=1a93dff0a22111e998fbb3b981677576; undefined=1a93dff0a22111e998fbb3b981677576; ssuid=1480618176; _ga=GA1.2.903235269.1562660375; _gid=GA1.2.678477229.1562660375; RTYCID=8c47f24e88bc404ab7ab3b13ca5c2c86; CT_TYCID=5a82281d672d4165aabaad01bbe2fda0; aliyungf_tc=AQAAAKe+mUtoxwwAuuz5cvNR0ONBk/gZ; csrfToken=n8V850lntGgDlmNhGBsbXb0o; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562730407; cloud_token=fd17ecd0236e46c9922bacd2cae78771; _gat_gtag_UA_123487620_1=1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522Quiet.G%2522%252C%2522integrity%2522%253A%252214%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2Mjc0NDY4NSwiZXhwIjoxNTk0MjgwNjg1fQ.fwN7K3WghcILj8jfXJLOMUxJQKpnYk8Rwo1MT6ZyzMlLe9uydGWTatceaWD9yV0Tt7iLFTls0YVj4V3y5nscnA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2Mjc0NDY4NSwiZXhwIjoxNTk0MjgwNjg1fQ.fwN7K3WghcILj8jfXJLOMUxJQKpnYk8Rwo1MT6ZyzMlLe9uydGWTatceaWD9yV0Tt7iLFTls0YVj4V3y5nscnA; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562744691'
print(add_cookie(c))
