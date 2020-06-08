# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    各种数据库的Python连接方法
    pip install pymysql
    pip install pymongo
    pip install redis
"""

import pymysql

# MySQL
mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="1111",
    db="",
    charset="utf8",
    # autocommit=True
)
cur = mydb.cursor()
cur.close()
mydb.close()

import pymongo

# MongoDB
myclient = pymongo.MongoClient("127.0.0.1", 28018)
myclient.close()

import redis

# Redis
mydb = redis.Redis(host="127.0.0.1", port=6379, password="1111", db=0)
mydb.close()
