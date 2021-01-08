# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
使用SSHTunnelForwarder隧道，通过跳板机链接服务器MongoDB
pip install sshtunnel
('59.110.148.238', 2052)：服务器Host与Port
ssh_username：服务器用户
ssh_password：服务器用户密码
ssh_pkey：服务器密钥文件本机地址
remote_bind_address：服务器MongoDB地址
local_bind_address：开启本地转发地址
返回格式：MongoDB链接对象
"""

import pymongo
from sshtunnel import SSHTunnelForwarder

# 隧道配置
server = SSHTunnelForwarder(
    ("59.110.148.238", 2052),
    ssh_username="root",
    ssh_pkey=r"C:\Users\Administrator\.ssh\my_rsa",
    remote_bind_address=("127.0.0.1", 27017),
    local_bind_address=("0.0.0.0", 28018),
)
# 开启隧道
server.start()
# 本地通过转发地址链接MongoDB
myclient = pymongo.MongoClient("127.0.0.1", 28018)
# 关闭服务
myclient.close()
# 关闭隧道
server.close()
