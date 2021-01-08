# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    遍历文件夹里所有文件,把文件路径加入队列
"""

import os
from queue import Queue


class File_Loop:
    def __init__(self):
        self.queue_file = Queue()

    def get_file(self):
        filedir = r"D:\test"
        for root, dirs, files in os.walk(filedir):
            for file in files:
                file_path = os.path.join(root, file)
                self.queue_file.put(file_path)

    def get_path(self):
        while 1:
            if self.queue_file.qsize() == 0:
                break
            path = self.queue_file.get()
            print(path)


if __name__ == "__main__":
    fl = File_Loop()
    fl.get_file()
    fl.get_path()
