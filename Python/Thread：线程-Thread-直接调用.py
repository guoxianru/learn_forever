# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import threading
import time
import traceback
from queue import Queue

import pandas as pd
import requests


class JdComments(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }
        self.req_queue = Queue()
        self.item_list = []

    def get_request(self, page):
        for page in range(page):
            url = (
                "https://club.jd.com/comment/productPageComments.action?&productId=100000177748&score=0&sortType=5&page="
                + str(page)
                + "&pageSize=10&isShadowSku=0&fold=1"
            )
            self.req_queue.put(url)

    def get_comment(self):
        # # 线程锁
        # threadLock = threading.Lock()
        # # 获得锁，成功获得锁定后返回True
        # # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # # 否则超时后将返回False
        # threadLock.acquire()
        while 1:
            print("剩余请求:%s" % self.req_queue.qsize())
            url = self.req_queue.get()
            try:
                response = requests.get(url=url, headers=self.headers)
                for res in response.json()["comments"]:
                    item = {}
                    item["昵称"] = res["nickname"]
                    item["评分"] = res["score"]
                    item["内容"] = res["content"].replace("\n", "").replace("\\n", "")
                    self.item_list.append(item)
            except:
                print("错误信息为:\n%s" % traceback.format_exc())
                print("当前请求：%s失败，重新加入队列！" % url)
                self.req_queue.put(url)
            time.sleep(3)
            # 向队列发送任务完成信号
            self.req_queue.task_done()
        # # 释放锁
        # threadLock.release()

    def save(self):
        pf = pd.DataFrame(self.item_list)
        pf.fillna("", inplace=True)
        pf.to_excel(r"test.xlsx", encoding="utf-8", index=False)


if __name__ == "__main__":
    jd = JdComments()
    jd.get_request(10)
    # 多线程
    for i in range(5):
        t = threading.Thread(target=jd.get_comment)
        # 守护线程
        t.daemon = True
        # 线程开启
        t.start()
        # # 线程阻塞
        # t.join()
    # 等待队列所有任务完成
    jd.req_queue.join()
    jd.save()
