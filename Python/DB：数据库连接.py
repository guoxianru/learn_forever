# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    各种数据库的Python连接方法
    pip install pymysql
    pip install pymongo
    pip install redis
"""

# MySQL
import pymysql

mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="1111",
    db="",
    charset="utf8",
    # 自动保存
    # autocommit=True
)
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
res = cur.fetchall()
cur.close()
mydb.close()

# MongoDB
import pymongo

myclient = pymongo.MongoClient(host="127.0.0.1", port=27017)
myclient.close()

# Redis
import redis

"""
redis://:password@host:port/db(TCP)
rediss://:password@host:port/db(TCP+SSL)
unix://:password@/path/to/socket.sock?db=db(UNIX+socket)
"""

rd0 = redis.Redis.from_url("redis://:password@127.0.0.1:6379/0")
# 连接池连接
pool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="password", db=1)
rd1 = redis.Redis(connection_pool=pool)
rd2 = redis.StrictRedis(connection_pool=pool)
# 直接连接
rd3 = redis.Redis(host="127.0.0.1", port=6379, password="password", db=1)
rd4 = redis.StrictRedis(host="127.0.0.1", port=6379, password="password", db=1)
