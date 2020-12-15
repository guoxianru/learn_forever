# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import requests


class JdComments(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }
        self.req_queue = Queue()

    def get_request(self, page):
        for page in range(page):
            url = (
                "https://club.jd.com/comment/productPageComments.action?&productId=100000177748&score=0&sortType=5&page="
                + str(page)
                + "&pageSize=10&isShadowSku=0&fold=1"
            )
            self.req_queue.put(url)

    def get_comment(self):
        while 1:
            print("剩余请求页:%s" % self.req_queue.qsize())
            if self.req_queue.empty():
                break
            item = {}
            url = self.req_queue.get()
            try:
                response = requests.get(url=url, headers=self.headers,)
                for res in response.json()["comments"]:
                    item["昵称"] = res["nickname"]
                    item["评分"] = res["score"]
                    item["内容"] = res["content"].replace("\\n", "")
            except:
                print("错误信息为:\n%s" % traceback.format_exc())
                print("当前请求：%s失败，重新加入队列！" % url)
                self.req_queue.put(url)
            time.sleep(3)


if __name__ == "__main__":
    jd = JdComments()
    jd.get_request(100)

    executor = ThreadPoolExecutor(max_workers=3)
    for i in range(2):
        executor.submit(jd.get_comment)
    # with ThreadPoolExecutor(3) as executor:
    #     executor.submit(jd.get_comment)
    # executor.map(jd.get_comment,range(10))
    # task2 = executor.map(jd.get_comment)
