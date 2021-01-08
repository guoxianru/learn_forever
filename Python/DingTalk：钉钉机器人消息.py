# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    钉钉机器人报警
    pip install requests
    pip install loguru
"""


def dingtalk(project, problem, phone="16619946646"):
    import json
    import requests
    from loguru import logger

    try:
        headers = {"Content-Type": "application/json"}
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "数据监控",
                "text": "# 数据监控\n1. 项目：{}\n2. 问题：{}\n2. 负责：@{}".format(
                    project, problem, phone
                ),
            },
            "at": {"atMobiles": [phone], "isAtAll": False},
        }
        json_data = json.dumps(data)
        response = requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=8c70af3ee95fd82cfefd5f82bdf2e5e8bc299433187b1241c2a9a2dbef5d9b2f",
            data=json_data,
            headers=headers,
        )
        if response.json()["errcode"] == 0:
            logger.info("钉钉机器人报警信息发送成功：%s\n" % response.json()["errmsg"])
        else:
            logger.error("钉钉机器人报警信息发送失败：%s\n" % response.json()["errmsg"])
    except:
        logger.error("钉钉机器人报警信息发送失败")


if __name__ == "__main__":
    dingtalk("微博登陆", "微博模拟登陆异常")
