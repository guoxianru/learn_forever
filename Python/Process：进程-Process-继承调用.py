# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import multiprocessing
import time
import traceback

import pandas as pd
import requests


class MyProcess(multiprocessing.Process):
    def __init__(self, req_queue, item_queue):
        super(MyProcess, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }
        self.req_queue = req_queue
        self.item_queue = item_queue

    def run(self):
        # # 进程锁
        # propessLock = multiprocessing.Lock()
        # # 获得锁，成功获得锁定后返回True
        # # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # # 否则超时后将返回False
        # propessLock.acquire()
        while 1:
            print("剩余剩余请求页:%s" % self.req_queue.qsize())
            url = self.req_queue.get()
            try:
                response = requests.get(url=url, headers=self.headers,)
                for res in response.json()["comments"]:
                    item = {}
                    item["昵称"] = res["nickname"]
                    item["评分"] = res["score"]
                    item["内容"] = res["content"].replace("\n", "").replace("\\n", "")
                    self.item_queue.put(list(item.items()))
            except:
                print("错误信息为:\n%s" % traceback.format_exc())
                print("当前请求：%s失败，重新加入队列！" % url)
                self.req_queue.put(url)
            time.sleep(3)
            # 向队列发送任务完成信号
            self.req_queue.task_done()
        # # 释放锁
        # propessLock.release()


class JdComments:
    def __init__(self):
        # 允许通知任务完成信号
        self.req_queue = multiprocessing.JoinableQueue()
        # 多进程安全的队列
        self.item_queue = multiprocessing.Queue()

    def get_request(self, page):
        for page in range(page):
            url = (
                "https://club.jd.com/comment/productPageComments.action?&productId=100000177748&score=0&sortType=5&page="
                + str(page)
                + "&pageSize=10&isShadowSku=0&fold=1"
            )
            self.req_queue.put(url)

    def get_comment(self):
        # 多进程
        for i in range(5):
            p = MyProcess(self.req_queue, self.item_queue)
            # 守护线程
            p.daemon = True
            # 线程开启
            p.start()
            # # 线程阻塞
            # p.join()

    def save(self):
        item_list = []
        for i in range(self.item_queue.qsize()):
            item = dict(self.item_queue.get())
            item_list.append(item)
        pf = pd.DataFrame(item_list)
        pf.fillna("", inplace=True)
        pf.to_excel(r"test.xlsx", encoding="utf-8", index=False)


if __name__ == "__main__":
    jd = JdComments()
    jd.get_request(10)
    jd.get_comment()
    # 等待队列所有任务完成
    jd.req_queue.join()
    jd.save()
