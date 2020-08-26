# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import time


def id2time(object_id):
    timeStamp = int(object_id[:8], 16)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timeStamp))


print(id2time("5d81ea973b955e5a80e22b3d"))
